# Resumen

# Aprender a automatizar el proceso de iteración en listas utilizando bucles y controles de iteración es fundamental para optimizar el manejo de datos en Python.
# ¿Cómo iterar una lista usando un bucle for?

# Para iterar sobre una colección de datos, podemos usar un bucle for. Aquí se muestra cómo acceder a cada elemento de una lista de números del 1 al 6:

# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     print(f"i es igual a: {i}")

# En este ejemplo, i representa cada elemento de la lista numbers.
# ¿Cómo iterar usando la función range?

# La función range permite generar una secuencia de números. Se puede especificar el inicio, el fin y el paso:

# for i in range(10):
#     print(i)  # Imprime del 0 al 9

# for i in range(3, 10):
#     print(i)  # Imprime del 3 al 9

# ¿Cómo usar condicionales dentro de un bucle for?

# Se pueden incluir condicionales dentro del bucle for para realizar operaciones específicas:

# frutas = ["manzana", "pera", "uva", "naranja", "tomate"]
# for fruta in frutas:
#     if fruta == "naranja":
#         print("naranja encontrada")
#     print(fruta)

# ¿Cómo funciona el bucle while?

# El bucle while ejecuta un bloque de código mientras se cumpla una condición:

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# ¿Qué hacer para evitar bucles infinitos?

# Es importante modificar la condición dentro del bucle while para evitar que se ejecute indefinidamente:

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# ¿Cómo usar break y continue en bucles?

# La palabra clave break se utiliza para salir del bucle prematuramente, mientras que continue omite la iteración actual y pasa a la siguiente:

# for i in numbers:
#     if i == 3:
#         break
#     print(i)  # Termina al llegar a 3

# for i in numbers:
#     if i == 3:
#         continue
#     print(i)  # Omite el 3

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:",i+1)

for i in range(3,10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

x = 0
while x<5:
    if x ==3:
        break
    print(x) 
    x +=1

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        break
    print("Aquí i es igual a:",i)