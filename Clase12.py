# Resumen

# Las matrices en Python son una herramienta poderosa que permite organizar datos en listas de listas, facilitando su manejo y manipulación.
# ¿Qué es una matriz en Python?

# Una matriz es una colección ordenada de datos dispuestos en filas y columnas. Se representa como una lista de listas, donde cada sublista es una fila de la matriz.
# ¿Cómo iterar a través de una matriz?

# Para iterar a través de una matriz en Python, se puede utilizar un bucle for anidado. Cada sublista (fila) se recorre individualmente:

#     Ejemplo de matriz:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

#     Iterar e imprimir cada elemento:

# for row in matrix:
#     for element in row:
#         print(element)

# ¿Cómo acceder a elementos específicos en una matriz?

# Para acceder a un elemento específico en una matriz, se utilizan los índices de la fila y la columna. Por ejemplo, para acceder al número 9 en la matriz anterior, se usa matrix[2][2].

#     Código:

# print(matrix[2][2])  # Salida: 9

# ¿Qué significa que las matrices sean mutables?

# Las matrices son mutables, lo que significa que se pueden modificar, añadir o eliminar elementos después de su creación. Este es un ejemplo básico:

#     Modificar un elemento:

# matrix[0][0] = 10
# print(matrix)  # Salida: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# ¿Cuál es la diferencia entre matrices y tuplas?

# A diferencia de las matrices, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. Las tuplas se utilizan para almacenar datos que no deben cambiar.

#     Ejemplo de tupla:

# numbers = (1, 2, 3)

# Intentar modificar una tupla genera un error:

# numbers[0] = 10  # Genera TypeError: 'tuple' object does not support item assignment

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])
numbers = 1,2,3,4,5
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = 'unos'
#print(numbers)