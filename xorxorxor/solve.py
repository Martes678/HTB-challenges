from binascii import unhexlify

def solve():
    hex_flag = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"
    
    data = unhexlify(hex_flag)
    
    prefix = "HTB{"
    key = []
    for i in range(4):
        key.append(data[i] ^ ord(prefix[i]))
    
    print(f"[*] Clave encontrada: {key} -> {[hex(k) for k in key]}")

    decoded_chars = []
    for i in range(len(data)):
        decoded_byte = data[i] ^ key[i % 4]
        decoded_chars.append(chr(decoded_byte))
    
    final_flag = "".join(decoded_chars)
    print(f"\n[+] Flag: {final_flag}")

if __name__ == "__main__":
    solve()