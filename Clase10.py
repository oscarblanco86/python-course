# Resumen

# Listas en Python nos facilita la tarea de permitir la manipulación y almacenamiento de datos diversos de manera estructurada y eficiente.
# ¿Cómo crear una lista en Python?

# Para iniciar, se crea una variable llamada todo utilizando corchetes para indicar que se trata de una lista. Dentro de los corchetes, se añaden los elementos separados por comas, por ejemplo:

# todo = ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]

# ¿Qué tipos de datos se pueden almacenar en una lista?

# Las listas en Python pueden almacenar múltiples tipos de datos, incluyendo cadenas, números enteros, números flotantes y valores booleanos. También pueden contener otras listas. Ejemplo:

# mix = ["string", 1, 2.5, True, [3, 4]]
# print(mix)

# ¿Cómo se determina la longitud de una lista?

# Para saber cuántos elementos hay en una lista, se usa la función len:

# print(len(mix))

# ¿Cómo se accede a elementos específicos de una lista?

# Se puede acceder a los elementos de una lista utilizando índices, donde el índice comienza en 0:

# print(mix[0])  # Primer elemento
# print(mix[-1])  # Último elemento

# ¿Cómo se realizan operaciones de slicing en listas?

# El slicing permite obtener sublistas a partir de una lista existente, especificando un rango de índices:

# print(mix[1:3])  # Desde el índice 1 hasta el 2 (el 3 no se incluye)
# print(mix[:2])  # Desde el inicio hasta el índice 1
# print(mix[2:])  # Desde el índice 2 hasta el final

# ¿Qué métodos de manipulación de listas existen?

#     Añadir elementos al final: append()

#     mix.append(False)
#     print(mix)

#     Insertar elementos en una posición específica: insert()

#     mix.insert(1, ["A", "B"])
#     print(mix)

#     Encontrar la primera aparición de un elemento: index()

#     print(mix.index(["A", "B"]))

#     Encontrar el mayor y menor elemento: max() y min()

#     numbers = [1, 2, 3.5, 90, 100]
#     print(max(numbers))
#     print(min(numbers))

# ¿Cómo se eliminan elementos de una lista?

#     Eliminar por índice: del

#     del numbers[-1]
#     print(numbers)

#     Eliminar una porción de la lista:

#     del numbers[0:2]
#     print(numbers)

#     Eliminar toda la lista:

#     del numbers

to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print("Testing", mix[0][1])
#print(numbers)