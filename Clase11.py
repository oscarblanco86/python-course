# Resumen

# Cuando asignamos una lista a una nueva variable, por ejemplo, B = A, no estamos creando una copia independiente. Ambas variables apuntan al mismo espacio de memoria. Así, cualquier cambio en A se reflejará en B.
# ¿Cómo evitar que dos listas apunten al mismo espacio de memoria?

# Para evitar que dos variables apunten al mismo espacio de memoria, debemos crear una copia superficial de la lista original usando slicing. Por ejemplo:

#     Crear una lista A con números del 1 al 5.
#     Asignar B = A y luego imprimir ambas listas muestra que ambas son idénticas.
#     Eliminar un elemento de A también lo elimina de B.

# ¿Cómo usar slicing para crear una copia de una lista?

# Podemos utilizar slicing para copiar una lista sin que ambas variables apunten al mismo espacio de memoria. Por ejemplo:

# A = [1, 2, 3, 4, 5]
# C = A[:]

# Luego, verificamos los IDs de memoria:

# print(id(A))
# print(id(C))

# Ambos IDs serán diferentes, lo que indica que C es una copia independiente de A.
# ¿Por qué es importante entender la asignación de memoria en listas?

# En Python, a diferencia de otros lenguajes, podemos almacenar diferentes tipos de datos en una colección. Entender cómo funciona la memoria es crucial para evitar errores en el código, especialmente en aplicaciones del mundo laboral.



a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c = a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)