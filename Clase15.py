# Resumen

# Una Comprehension List es una forma concisa de crear listas en Python, pues permite generar listas nuevas transformando cada elemento de una colección existente o creando elementos a partir de un rango. La sintaxis es compacta y directa, lo que facilita la comprensión del propósito de tu código de un vistazo.

# La estructura básica de una Comprehension List es:

# [expresión for elemento in iterable if condición]

# Que se traduce a: “Crea una nueva lista evaluando nueva_expresión para cada elemento en el iterable.”
# Ejercicios:

#     Doble de los Números
#     Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

#     Filtrar y Transformar en un Solo Paso
#     Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

#     Crear un Diccionario con List Comprehension
#     Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

#     Anidación de List Comprehensions
#     Dada una lista de listas (una matriz):

#     pythonCopiar código
#     matriz = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     Calcula la matriz traspuesta utilizando una List Comprehension anidada.

#     Extraer Información de una Lista de Diccionarios
#     Dada una lista de diccionarios que representan personas:

#     pythonCopiar código
#     personas = [
#         {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#         {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#         {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#         {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
#     ]

#     Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

#     List Comprehension con un else
#     Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

# Soluciones

#     Doble de los Números

#     pythonCopiar código
#     numeros = [1, 2, 3, 4, 5]
#     dobles = [x * 2 for x in numeros]
#     print("Dobles:", dobles)

#     Filtrar y Transformar en un Solo Paso

#     pythonCopiar código
#     palabras = ["sol", "mar", "montaña", "rio", "estrella"]
#     palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
#     print("Palabras filtradas y en mayúsculas:", palabras_filtradas)

#     Crear un Diccionario con List Comprehension

#     pythonCopiar código
#     claves = ["nombre", "edad", "ocupación"]
#     valores = ["Juan", 30, "Ingeniero"]

#     diccionario = {claves[i]: valores[i] for i in range(len(claves))}
#     print("Diccionario creado:", diccionario)

#     Anidación de List Comprehensions

#     pythonCopiar código
#     matriz = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
#     print("Transpuesta con List Comprehension:", transpuesta_comprehension)

#     Extraer Información de una Lista de Diccionarios

#     pythonCopiar código
#     personas = [
#         {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#         {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#         {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#         {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
#     ]

#     nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
#     print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid

#     List Comprehension con un else

#     pythonCopiar código
#     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
#     print("Números transformados:", transformados)

# Las Comprehension Lists en Python son una herramienta poderosa y versátil que permite escribir código más limpio y eficiente. Al dominar su uso, puedes realizar transformaciones y filtrados de datos de manera más concisa, lo que no solo mejora la legibilidad del código, sino que también puede optimizar su rendimiento.

# Practicar con ejemplos como los presentados te ayudará a integrar esta técnica en tus proyectos de programación diaria, facilitando la manipulación de colecciones de datos de manera elegante y efectiva.


squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print("Temperatura en F:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x % 2 == 0]
print("Numeros pares: ", evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("matrix: \n",matrix)
print("transposed matrix: \n",transposed)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)