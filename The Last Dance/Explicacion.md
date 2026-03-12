El reto consiste en romper el cifrado ChaCha20 en el que se reutilizan las claves. <br>
Primero hay que comprobar cómo se encriptan los mensajes en el script source.py <br>
La vulnerabilidad que se ha encontrado en el cifrado es: <br>
&emsp;- Se reutiliza la clave para cifrar _encrypted_message_ y _encrypted_flag_. <br>
&emsp;- Se usa la operación XOR con la misma clave. <br>

Una vez conocida una vulnerabilidad explotable, se crea solve.py en donde:
&emsp; 1. Recuperar la clave <br>
&emsp;&emsp;Como se usa el mensaje que se da en source.py y se almacena en la variable _p1_. <br>
&emsp;&emsp;Posteriormente se hace una operación XOR con _p1_ y su mensaje cifrado. <br>
&emsp; 2. Obtener la Flag <br>
&emsp;&emsp;Una vez obtenida la clave, mediante una operación XOR se obtiene la Flag en texto plano, ya que conocemos la Flag cifrada. <br>
