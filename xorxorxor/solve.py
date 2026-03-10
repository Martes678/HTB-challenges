from binascii import unhexlify

hexflag = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"

flag = unhexlify(hexflag)

conocido = "HTB{"
clave = []
for i in range(4):
    clave.append(flag[i] ^ ord(conocido[i]))

print(f"Clave encontrada: {clave}")

descifrado = []
for i in range(len(flag)):
    decoded_byte = flag[i] ^ clave[i % 4]
    descifrado.append(chr(decoded_byte))

texto = "".join(descifrado)
print(f"Flag: {texto}")