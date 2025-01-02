# Resumen

# Los diccionarios en Python son una estructura que almacenan dos datos, la clave y el valor. Un ejemplo cotidiano es un diccionario físico donde buscamos el significado de una palabra y encontramos la palabra (clave) y su definición (valor). Veamos cómo se utilizan en código.
# ¿Cómo se crea un diccionario en Python?

# Iniciamos creando una variable llamada numbers y especificamos el uso de diccionarios utilizando llaves. Asignamos valores a las claves:

# numbers = {1: "one", "2": "two", 3: "three"}
# print(numbers)

# ¿Cómo se accede a los elementos de un diccionario?

# Para consultar la información de una clave específica, utilizamos la indexación:

# print(numbers["2"])

# ¿Cómo se eliminan elementos de un diccionario?

# Para eliminar un elemento, utilizamos la clave del mismo:

# del information["edad"]
# print(information)

# ¿Qué métodos existen para trabajar con diccionarios?

# Podemos utilizar métodos propios de los diccionarios, como keys(), values(), e items():

# # Obtener las claves
# claves = information.keys()
# print(claves)

# # Obtener los valores
# valores = information.values()
# print(valores)

# # Obtener los pares clave-valor
# pares = information.items()
# print(pares)

# ¿Cómo se crea un diccionario de diccionarios?

# Podemos crear una agenda de contactos usando diccionarios de diccionarios:

# contactos = {
#     "Carla": {"apellido": "Florida", "altura": 1.7, "edad": 30},
#     "Diego": {"apellido": "Antesana", "altura": 1.75, "edad": 32}
# }
# print(contactos["Carla"])

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Carla",
               "Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["Carla"])