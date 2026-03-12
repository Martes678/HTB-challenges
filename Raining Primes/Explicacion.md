Este reto consiste en descifrar un mensaje mediante el forzamiento del cifrado AES y la factorización para romper el cifrado RSA. <br>
Para poder descifrar el mensaje, hay que analizar el script server.py, el cual realiza: <br>
&emsp;-Solicitar números primos, opción 1 <br>
&emsp;&emsp;En esta sección devuelve un número primo, los cuales se generan con la fórmula p = a * r + b. <br>
&emsp;&emsp;a y b son números aleatorios grandes y r es un secreto <br>
&emsp;-Cifrar la Flag con cifrado AES y RSA <br>
&emsp;&emsp;La Flag es cifrada con cifrado AES y posteriormente con cifrado RSA <br>
&emsp;-Actualizar clave AES <br>
&emsp;&emsp;Permite forzar la clave AES a 0 <br>
&emsp;-Obtener el mansaje con los valores de RSA, opción 3 <br>
&emsp;&emsp;La opción 2, da los valores del módulo, el exponente y el mensaje cifrado. <br>

Una vez entendido el funcionamiento de server.py, se realiza solve.py, en donde: <br>
&emsp; 1. Haz que obtener el valor de _r_ de la generación de números primos. <br>
&emsp;&emsp;Para ello se usa la matriz _LLL_. <br>
&emsp;&emsp;Como el valor común de todos los números primos es r, con la matriz _LLL_, se puede dejar expuesto el valor de _r_. <br>
&emsp; 2. Romper AES <br>
&emsp;&emsp;Una vez obtenido el valor de _r_, se puede romper el cifrado AES, ya que el server calcula el valor de la clave AES con _r_. <br>
&emsp;&emsp;Al enviarle el valor correcto de _r_, el módulo del cálculo da 0 gracias a la función _update_key()_. <br>
&emsp;3. Factorizacion de _n_ de RSA <br>
&emsp;&emsp;Se factoriza el valor de _n_ obtenido con la opción 3 mediante raíces cuadradas. <br>
&emsp;&emsp;Como además se conoce que p = a * r + b, sólo se necesita obtener el valor de _q_, ya que n = p * q. <br>
&emsp;4. Descfrar la Flag <br>
&emsp;&emsp;Una vez conocido _p_ y _q_, se descifra el mensaje, obteniendo así la Flag. <br>
