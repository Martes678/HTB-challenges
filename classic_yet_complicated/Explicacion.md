Este reto consiste en descifrar el mensaje sin conocer la clave dell cifrado Vigenère. Para ello, se ha usado el método Kasiski con ayuda de las frecuencias de cada letra
del inglés. <bre>
Primero, se han introducido el índice de coincidencia en la variable _frecuencia_, donde la posición 0 es el IC de la letra _A_, la posición 1 el IC de la letra _B_, y así hasta la letra _Z_.
<bre>En la función _romper_cifrado()_, es donde se obtiene la longitud de la clave Vigenère, y el valor. <bre>
Para ello, se verifican longitudes de clave de hasta longitud 20, y se calculan los índices de coincidencia. Mientras más alto el índice de coincidencia, mayor es la probabilidad de que sea esa longitud.
El IC máximo será el del tamaño de la clave. <bre>
Una vez se conoce la longitud más probable, se obtiene la clave con ayuda de la varibale _frecuencia_, donde se almacenan las frecuencias de cada letra. A partir de ahí, se 
reconstruye la clave con el desplazamiento que mejor encaje en cada posición. <bre>
Por último, una vez conocida la clave, se descifra el mansaje para verificar que es correcta la clave.
