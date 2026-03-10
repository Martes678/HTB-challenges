import collections

frecuencias = [0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 
               0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 
               0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 
               0.0197, 0.0007]

def romper_cifrado(texto):
    descifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            descifrado = descifrado + caracter.upper()

    longitud = 1
    indice = 0
    #La clave que devuelve es de longitud 20
    for largo in range(1, 21): #Si no da resultados se puede poner que la longitud de la clave sea más grande
        columnas = []
        for i in range(largo):
            columnas.append("")
            
        for i in range(len(descifrado)):
            c = descifrado[i]
            columna_idx = i % largo
            columnas[columna_idx] = columnas[columna_idx] + c
            
        total = 0
        for col in columnas:
            n = len(col)
            if n > 1:
                cuenta = collections.Counter(col)
                suma = 0
                for f in cuenta.values():
                    suma = suma + (f * (f - 1))
                valorc = suma / (n * (n - 1))
                total = total + valorc
        
        promedio = total / largo
        if promedio > indice:
            indice = promedio
            longitud = largo
            
    clave = ""
    for i in range(longitud):
        columna = ""
        for j in range(i, len(descifrado), longitud):
            columna = columna + descifrado[j]
        
        desplazamiento = 0
        punt = -1
        
        for s in range(26):
            score = 0
            for char in columna:
                indice = (ord(char) - 65 - s) % 26
                score = score + frecuencias[indice]
            
            if score > punt:
                punt = score
                desplazamiento = s
        
        clave = clave + chr(desplazamiento + 65)
        
    return clave.lower()

def descifrar_vigenere(texto, clave):
    clave = clave.lower()
    longitud = len(clave)
    resultado = []
    pos = 0
    
    for caracter in texto:
        if caracter.isalpha():
            base = 65 if caracter.isupper() else 97
            c_val = ord(caracter) - base
            k_val = ord(clave[pos % longitud]) - 97
            descifrado = chr((c_val - k_val) % 26 + base)
            resultado.append(descifrado)
            pos += 1
        else:
            resultado.append(caracter)
            
    return "".join(resultado)

texto = "alp gwcsepul gtavaf, nlv prgpbpsu mb h jcpbyvdlq, ipltga rv glniypfa we ekl 16xs nsjhlcb. px td o lccjdstslpahzn fptspf xstlxzi te iosj ezv sc xcns ttsoic lzlvrmhaw ez sjqijsa xsp rwhr. tq vxspf sciov, alp wsphvcv pr ess rwxpqlvp nwlvvc dyi dswbhvo ef htqtafvyw hqzfbpg, ezutewwm zcep xzmyr o scio ry tscoos rd woi pyqnmgelvr vpm . qbctnl xsp akbflowllmspwt nlwlpcg, lccjdstslpahzn fptspfo oip qvx dfgysgelipp ec bfvbxlrnj ojocjvpw, ld akfv ekhr zys hskehy my eva dclluxpih yoe mh yiacsoseehk fj l gebxwh sieesn we ekl iynfudktru. xsp yam zd woi qwoc."
print(romper_cifrado(texto))
print(descifrar_vigenere(texto,romper_cifrado(texto)))