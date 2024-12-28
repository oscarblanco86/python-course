# Resumen

# En Python, cuando trabajamos con proyectos que requieren interacción del usuario, es común solicitar datos como correo o contraseña para ejecutar acciones específicas. Este mismo enfoque es útil para entender la función input.
# ¿Cómo se recibe información del usuario en Python?

# Para recibir información del usuario desde la consola, creamos una variable y asignamos el resultado de la función input. Por ejemplo, para pedir el nombre del usuario:

# nombre = input("Ingrese su nombre: ")
# print(nombre)

# Al ejecutar este código, se habilita una sección para introducir información. Ingresamos un nombre, presionamos Enter y se imprime el valor guardado en la variable nombre.
# ¿Qué ocurre si eliminamos la función print?

# Si eliminamos print y ejecutamos el código, el nombre ingresado no se mostrará en la consola:

# nombre = input("Ingrese su nombre: ")

# Para ver el resultado, es imprescindible usar print.

# Podemos solicitar la edad del usuario creando una variable edad y utilizando input, luego imprimimos ambos valores:

# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# print(nombre)
# print(edad)

# Al ejecutar, ingresamos el nombre y la edad, y ambos valores se muestran en pantalla.
# ¿Cuál es el tipo de dato devuelto por input?

# El resultado de input es siempre un string, incluso si ingresamos un número. Podemos verificar el tipo de dato usando type:

# name = input("Ingrese su nombre: ")
# age = input("Ingrese su edad: ")
# print(type(name))
# print(type(age))

# Al ejecutar, se mostrará que ambos valores son de tipo str.
# ¿Cómo se convierte el tipo de dato (casting)?

# Si queremos que la edad sea un número entero en lugar de un string, usamos el casting:

# age = int(input("Ingrese su edad: "))

# Ejecutamos y verificamos que age ahora es un entero. También podemos convertir a otros tipos de datos, como flotantes:

# age = float(input("Ingrese su edad: "))

# ¿Qué sucede si ingresamos un dato inesperado?

# Si el código espera un entero, pero ingresamos un string, se produce un ValueError. Es importante manejar el tipo de datos correctamente para evitar errores:


name = input("Ingrese su nombre: ")
print(name)
print(type(name))
age = int(input("Ingrese su edad: "))
print(type(age))