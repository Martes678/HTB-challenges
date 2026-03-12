#!/usr/bin/env python3
from pwn import *
from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from math import gcd, isqrt

HOST = '154.57.164.74'
PORT = 31018

A, B, R = 384, 256, 640

def recover_r(muestras):
    WA1 = Integer(2)**(A + 1)
    WAB = Integer(2)**(A + B)
    xs = [Integer(xi) for xi in muestras]

    for dim in range(2, len(xs) + 1):
        vals = xs[:dim]
        M = Matrix(ZZ, dim, dim)
        M[0, 0] = 1
        for j in range(1, dim):
            M[0, j] = vals[j]
        for i in range(1, dim):
            M[i, i] = -vals[0]
        W = diagonal_matrix([WA1] + [WAB] * (dim - 1))
        Lr = (M * W).LLL()
        Ld = Lr / W

        print(f"[+] LLL dim={dim}...", end=' ', flush=True)
        for k in range(dim):
            t1 = abs(int(Ld[k][0]))
            if not t1 or not (A - 10 <= t1.bit_length() <= A + 10):
                continue
            r_cand = int(vals[0]) // t1
            if not (R - 10 <= r_cand.bit_length() <= R + 10):
                continue
            checks = [Integer(xi % r_cand).bit_length() for xi in vals]
            if all(c <= B + 4 for c in checks):
                print(f"listo.  r={r_cand.bit_length()}b (dim={dim}) ")
                return r_cand
            for delta in range(-5, 6):
                rc = r_cand + delta
                if rc <= 0: continue
                if all(Integer(xi % rc).bit_length() <= B + 4 for xi in vals):
                    print(f"listo.  r={rc.bit_length()}b (delta={delta}) ")
                    return rc
        print("listo.")
    return None

def factorizar_n(n_val, r):
    s = n_val % r
    middle = (n_val - s) // r
    M0 = middle % r
    M1 = middle // r

    for k in range(5):
        C_try = M0 + k * r
        U_try = M1 - k
        if U_try <= 0:
            continue
        disc  = C_try * C_try - 4 * U_try * s
        if disc < 0:
            continue
        sq = isqrt(disc)
        if sq * sq != disc:
            continue
        for z in [(C_try + sq) // 2, (C_try - sq) // 2]:
            if z <= 0:
                continue
            g = gcd(z * r + s, n_val)
            if 1 < g < n_val and (n_val // g) * g == n_val:
                p_f, q_f = int(g), int(n_val // g)
                print(f"[+] p={p_f.bit_length()}b, q={q_f.bit_length()}b (k={k})")
                return p_f, q_f
    return None, None


def solve():
    io = remote(HOST, PORT)

    num = 20
    print(f"[+] Recolectando {num} primos...")
    muestras = []
    for i in range(num):
        io.sendlineafter(b"> ", b"1")
        io.recvuntil(b"primes!\n")
        muestras.append(int(io.recvline().strip()))
        print(f"  [{i:02d}] {muestras[-1].bit_length()} bits")

    print("\n[+] Recuperando r...")
    r = recover_r(muestras)

    if r is None:
        print("[-] r no recuperado.")
        io.sendlineafter(b"> ", b"3")
        io.recvuntil(b"flag:\n")
        n_r, e_r, c_r = eval(io.recvline().decode().strip())
        print(f"n={n_r}\ne={e_r}\nc={c_r}")
        io.close()
        return

    print(f"[*] r = {r.bit_length()} bits")

    # Forzar AES key = 0:  k1_i = 2r  =>  (b_i·2r) mod r = 0  =>  bit_i = 0
    print("[+] Forzando AES key = 0  (k1_i = 2·r)...")
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"key:\n", str([r * 2] * 256).encode())

    io.sendlineafter(b"> ", b"3")
    io.recvuntil(b"flag:\n")
    n_rsa, e_rsa, c_rsa = eval(io.recvline().decode().strip())
    io.close()
    print(f"[*] n = {n_rsa.bit_length()} bits")

    print("[+] Factorizando n...")
    p, q = factorizar_n(n_rsa, r)
    if p is None:
        print("[-] Factorización fallida.")
        return

    phi = (p - 1) * (q - 1)
    d = pow(e_rsa, -1, phi)
    m = pow(c_rsa, d, n_rsa)

    ct = long_to_bytes(m)
    while len(ct) % 16:
        ct = b'\x00' + ct

    dec = AES.new(b'\x00' * 32, AES.MODE_ECB).decrypt(ct)
    try:
        flag = unpad(dec, 16).decode()
    except Exception:
        flag = dec.hex()
        if b'HTB{' in dec:
            flag = dec[dec.index(b'HTB{'):].decode(errors='replace')

    print("\n" + "=" * 55)
    print(f"  FLAG: {flag}")
    print("=" * 55)


if __name__ == "__main__":
    solve()