from pwn import remote
from Crypto.Util.number import bytes_to_long, long_to_bytes
from math import gcd
import time

HOST = "" #Direccion
PORT = 0 #Numero del puerto
K = 0x13373
NUM_QUERIES = 20

def invert_base_key(generated_key):
    tmp0 = (generated_key >> 450) & ((1 << 50) - 1)
    kh = tmp0 >> 25
    kl = tmp0 & ((1 << 25) - 1)
    for _ in range(25):
        temp_kh = kl ^ kh
        kl = kh
        kh = temp_kh
    return (kh << 25) | kl

def crt_combine(r1, m1, r2, m2):
    g = gcd(m1, m2)
    if (r2 - r1) % g != 0:
        return None, None
    lcm = (m1 * m2) // g
    inv = pow(m1 // g, -1, m2 // g)
    t = ((r2 - r1) // g * inv) % (m2 // g)
    res = (r1 + m1 * t) % lcm
    return res, lcm

io = remote(HOST, PORT)
base_keys = []
print(f"Recolectando claves...")
io.recvuntil(b"quit): ")

for _ in range(NUM_QUERIES):
    io.sendline(b"")
    line = io.recvline().decode().split("Encrypted Message: ")[1].strip()
    gen_key = bytes_to_long(bytes.fromhex(line))
    base_keys.append(invert_base_key(gen_key))
io.close()

t_start = int(time.time())
for nonce in range(t_start - 200, t_start + 200):
    r = base_keys[0]
    m = (nonce + 0) * K
    possible = True
    for i in range(1, len(base_keys)):
        r_new, m_new = crt_combine(r, m, base_keys[i], (nonce + i) * K) 
        if r_new is None:
            possible = False
            break
        r = r_new
        m = m_new
    
    if possible:
        flag = long_to_bytes(r)
        if b"HTB{" in flag:
            print(f"Nonce: {nonce}")
            print(f"Flag: {flag.decode()}")
            break
else:
    print("No se encontró la flag.")