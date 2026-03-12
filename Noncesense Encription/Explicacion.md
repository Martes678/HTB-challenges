Este reto consiste en obtener la flag mediante la implementación de un código en el que explote las vulnerabilidades que tiene implementar un cifrado no seguro.
En server.py, script donde se implementa el cómo se cifra una cadena de carácteres, se puede ver varias vulnerabilidades, las cuales son: <br>
&emsp;1. Uso de semilla no aleatoria para el nonce. <br>
&emsp;&emsp;El mecanismo de cifrado usa el tiempo como semilla, para cifrar el mensaje. <br>
&emsp;&emsp;Por lo tanto, si se sabe el momento en el que se ha cifrado el mensaje, se puede conocer la semilla.<br>
&emsp;2. Uso de operaciones XOR y desplazamientos <br>
&emsp;&emsp;La clave new_key se genera mediante una serie de pasos lineales. <br>
&emsp;&emsp;Como no hay confusión en el cifrado, es sencillo conociedo los pasos que se hacen para cifrar, hacer los pasos inversos. <br>
&emsp;3. La key se crea con módulo <br>
&emsp;&emsp;La Flag se usa como dividendo en una operación de módulo, permitiendo ataques de recuperación de residuos. <br>
&emsp;&emsp;key = self.generator % ((self.nonce + self.counter) * self.k) <br>

Una vez conocidas las vulnerabilidades del cómo se crea la key y el cómo se cifra el mensaje, se crea un script que explota las vulnerabilidades anteriormente nombradas. <br>
Para ello se usan diferentes funciones: <br>
&emsp;-invert_base_key(): <br>
&emsp;&emsp;Esta función invierte la función __gen_key() de server.py. <br>
&emsp;&emsp;Por lo tanto, revierte las operaciones XOR y desplazamientos hechos en la encripación. <br>
&emsp;-crt_combine(): <br>
&emsp;&emsp;Esta función es la que permite mediante los residuos obtener el nonce y base_key mediante el teorema del resto chino.  
&emsp;&emsp;Como se conoce base_key y nonce, se puede descifrar el mesaje. <br>
