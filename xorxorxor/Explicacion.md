Este reto consiste en descifrar la flag dada en output.txt mediante la operación XOR. <bre>
Como se conoce el formato de la flag (HTB{...}), se explota esa vulnerabilidad para conocer la clave XOR. <bre>
Se obtine la clave seleccionando los primeros 4 carácteres conocidos, y con ellos, se obtiene la clave gracias a que nos dan el texto cifrado en output.txt. <bre>
Una vez obtenida la clave se descifra el mensaje entero para así obtener la Flag en texto claro.
