# Resumen

# En el mundo de la programación con Python, las operaciones matemáticas básicas como la suma, resta, multiplicación y división son fundamentales. Sin embargo, Python ofrece operaciones adicionales que expanden nuestras posibilidades.
# ¿Cómo realizamos las operaciones matemáticas básicas en Python?

# Primero, creamos dos variables: a con valor 10 y b con valor 3. Usamos comentarios para indicar que estamos trabajando con operadores numéricos. Imprimimos los resultados de las cuatro operaciones básicas:

# a = 10
# b = 3
# print("Suma:", a + b)
# print("Resta:", a - b)
# print("Multiplicación:", a * b)
# print("División:", a / b)

# ¿Qué es el operador módulo y cómo se usa?

# El operador módulo (%) obtiene el residuo de una división. Por ejemplo, 13 % 5 devuelve 3. En Python, se usa así:

# a = 13
# b = 5
# print("Módulo:", a % b)

# ¿Qué sucede al dividir por cero en Python?

# Dividir por cero genera un error. Para ilustrarlo:

# a = 10
# b = 0
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("Error: División por cero")

# ¿Qué es la división de enteros y cómo se implementa?

# La división de enteros (//) devuelve solo la parte entera de una división. Por ejemplo:

# a = 10
# b = 3
# print("División Entera:", a // b)

# ¿Cómo se realiza la potenciación en Python?

# La potenciación se representa con **. Para elevar 10 al cubo, usamos:

# a = 10
# b = 3
# print("Potenciación:", a ** b)

# ¿Qué es PEMDAS y cómo afecta nuestras operaciones?

# PEMDAS es la regla de prioridad de operaciones: Paréntesis, Exponentes, Multiplicación y División (de izquierda a derecha), Adición y Sustracción (de izquierda a derecha). Veamos un ejemplo:

# operation = (2 + 3) * 4
# print(operation)  # Resultado: 20

# ¿Cómo se manejan los operadores booleanos en Python?

# Los operadores booleanos comparan valores y devuelven True o False. Ejemplos:

# a = 10
# b = 3
# print(a > b)  # True
# print(a < b)  # False
# print(a == b)  # False
# print(a != b)  # True

# Estos operadores nos ayudan a tomar decisiones en el código, permitiendo crear condiciones y bucles efectivos.


#Operadores numéricos
a = 10
b = 10
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la división:", a // b)
print("Módulo:", a % b)
a /= 2
print(a)
operation_1  = 2 + 3 * 4
operation_2  = (2 + 3) * 4
print(operation_1)
print(operation_2)
operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_3)

# operadores_comparación


a = 10
b = 3
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)