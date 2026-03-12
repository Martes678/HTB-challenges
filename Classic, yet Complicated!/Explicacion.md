Este reto consiste en descifrar el mensaje sin conocer la clave dell cifrado Vigenère. <br>
Para ello, se ha usado el método Kasiski con ayuda de las frecuencias de cada letra del inglés. <br>
Primero, se han introducido el índice de coincidencia en la variable frecuencia, donde la posición 0 es el IC de la letra A, la posición 1 el IC de la letra B, y así hasta la letra Z. <br>
En la función romper_cifrado(), es donde se obtiene la longitud de la clave Vigenère, y el valor. Para ello, se verifican longitudes de clave de hasta longitud 20, y se calculan los índices de coincidencia. 
Mientras más alto el índice de coincidencia, mayor es la probabilidad de que sea esa longitud, por lo que el IC máximo será el del tamaño de la clave. <br>
Una vez se conoce la longitud más probable, se obtiene la clave con ayuda de la varibale frecuencia, donde se almacenan las frecuencias de cada letra. <br>
A partir de ahí, se reconstruye la clave con el desplazamiento que mejor encaje en cada posición. Por último, una vez conocida la clave, se descifra el mansaje para verificar que es correcta la clave.
