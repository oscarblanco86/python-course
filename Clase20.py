# Resumen
# ¿Cómo utilizar lambda para operaciones básicas?

# Para realizar operaciones sencillas con lambda, no necesitamos especificar el nombre de la función. Solo requerimos parámetros y la operación deseada. Por ejemplo, para sumar dos números, podemos definir una función lambda así:

# sumar = lambda a, b: a + b
# print(sumar(10, 4))

# ¿Cómo utilizar lambda para multiplicaciones?

# Podemos adaptar fácilmente lambda para realizar otras operaciones como la multiplicación:

# multiplicar = lambda a, b: a * b
# print(multiplicar(80, 4))

# ¿Cómo aplicar lambda a elementos de una lista con map?

# Cuando trabajamos con listas y queremos aplicar una función a cada elemento, map es útil junto con lambda. Por ejemplo, para obtener el cuadrado de los números del 0 al 10:

# numeros = list(range(11))
# cuadrados = list(map(lambda x: x ** 2, numeros))
# print("Cuadrados:", cuadrados)

# ¿Cómo filtrar elementos de una lista con lambda y filter?

# Lambda también es útil para filtrar elementos que cumplen ciertas condiciones. Por ejemplo, para obtener los números pares de una lista:

# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# print("Pares:", numeros_pares)

# Como hemos visto, lambda ofrece una forma más sencilla de trabajar con funciones en Python sin comprometer su eficiencia. En la próxima clase, exploraremos temas más complejos donde las funciones serán el foco principal.


add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", squared_numbers )

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)