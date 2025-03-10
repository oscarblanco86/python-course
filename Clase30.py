# ¿Cómo trabajar con archivos de texto en Python?

# Uno de los aspectos más poderosos de Python es su capacidad para interactuar con archivos de texto, y no solo con variables como lo hemos hecho hasta ahora. Desde archivos TXT hasta CSV y JSON, Python facilita la lectura, escritura, y modificación de archivos externos. Imagina tener la capacidad de acceder a un cuento clásico, como el de Caperucita Roja, para extraer, manipular y enriquecer datos. Vamos a explorar cómo hacerlo paso a paso.
# ¿Cómo abrir y leer un archivo en Python?

# Para leer un archivo en Python, primero es necesario abrirlo utilizando la función open(). Supongamos que queremos leer un archivo llamado caperucita.txt:

# # Abrimos el archivo en modo lectura
# with open("caperucita.txt", "r") as file:
#     # Leemos cada línea y eliminamos los saltos de línea al final
#     for line in file:
#         print(line.strip())

#     open("caperucita.txt", "r"): Abre el archivo en modo lectura.
#     line.strip(): Quita los espacios y saltos de línea al final de cada línea.

# ¿Cómo almacenar líneas de un archivo en una lista?

# Si deseas almacenar todas las líneas de un archivo en una lista, puedes emplear el método readlines(). Esto es especialmente útil si planeas manipular o analizar el contenido posteriormente.

# # Abrimos el archivo y almacenamos las líneas en una lista
# with open("caperucita.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# Este código:

#     Carga todas las líneas del archivo en una lista llamada lines.
#     Las líneas incluyen los caracteres de salto de línea \n.

# ¿Cómo escribir o añadir texto en un archivo?

# Hay casos donde necesitarás modificar el contenido de un archivo, sea para agregar nueva información o sobreescribirla. Aquí es donde los modos de escritura (w para escribir) y anexar (a para añadir) se vuelven esenciales.
# Añadiendo texto al final sin borrar el contenido existente

# Para añadir texto al final del archivo sin eliminar el contenido previo, se utiliza el modo a:

# # Abrimos el archivo en modo añadir y escribimos una línea al final
# with open("caperucita.txt", "a") as file:
#     file.write("\n\nBy:ChatGPT.")

# Sobreescribiendo un archivo

# Para sobreescribir todo el contenido, se utiliza el modo w, pero es fundamental tener cuidado, ya que esto eliminará todo el texto existente. Aquí un ejemplo:

# # Abrimos el archivo en modo escritura y sobreescribimos su contenido
# with open("caperucita.txt", "w") as file:
#     file.write("\n\nBy:ChatGPT.")

# ¿Cuáles son los beneficios de automatizar tareas de archivo con Python?

# La capacidad de Python para manejar archivos es una puerta abierta a la automatización de tareas mediante scripting. Esto permite procesos eficientes de lectura y manipulación de datos, ahorrando tiempo y esfuerzos repetitivos. Por ejemplo, podrías crear un script que automáticamente analice y procese varios archivos de texto.
# Desafío: ¿Cuántas líneas tiene el cuento de Caperucita Roja?

# Ahora, te dejo un reto: cuenta el número de líneas en el archivo caperucita.txt y comparte tu resultado en los comentarios. Este ejercicio no solo reforzará tus habilidades, sino que también te acercará a comprender el poder del manejo de archivos en Python.

# ¡Sigue explorando y practicando para dominar estas habilidades! Python ofrece un camino rico en posibilidades para interactuar con datos y archivos de manera eficiente y efectiva.


#Leer un archivo línea por línea
# with open('cuento.txt', 'r') as file:
#     for lineas in file:
#         print(lineas.strip())

#Leer todas las líneas en una lista
with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#Añadir texto
# """with open('caperucita.txt', 'a') as file:
#     file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
# with open('caperucita.txt', 'w') as file:
#     file.write("\n\nBy:ChatGPT")