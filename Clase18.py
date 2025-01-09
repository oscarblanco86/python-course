# Resumen

# Trabajar con iteradores y generadores en Python permite manejar grandes cantidades de datos de manera eficiente, sin necesidad de cargar todo en memoria.
# ¿Qué es un iterador y cómo se usa?

# Un iterador en Python es un objeto que permite recorrer todos los elementos de una colección, uno a la vez, sin necesidad de usar índices. Para crear un iterador, se utiliza la función iter() y para obtener el siguiente elemento, se usa la función next(). Veamos un ejemplo:

# # Crear una lista
# lista = [1, 2, 3, 4]

# # Obtener el iterador de la lista
# iterador = iter(lista)

# # Usar el iterador para obtener elementos
# print(next(iterador))  # Imprime: 1
# print(next(iterador))  # Imprime: 2
# print(next(iterador))  # Imprime: 3
# print(next(iterador))  # Imprime: 4

# # Intentar obtener otro elemento después de finalizar la iteración
# print(next(iterador))  # Esto generará una excepción StopIteration

# Los iteradores también pueden recorrer cadenas de texto:

# # Crear una cadena
# texto = "hola mundo"

# # Obtener el iterador de la cadena
# iterador_texto = iter(texto)

# # Iterar a través de la cadena
# for caracter in iterador_texto:
#     print(caracter)

# ¿Cómo crear un iterador con range para números impares?

# La función range se puede usar para crear un iterador que recorra números impares:

# # Crear un iterador para números impares hasta 10
# limite = 10
# iterador_impares = iter(range(1, limite + 1, 2))

# # Iterar a través de los números impares
# for numero in iterador_impares:
#     print(numero)

# Para cambiar a números pares, solo se debe modificar el inicio del rango:

# # Crear un iterador para números pares hasta 10
# iterador_pares = iter(range(0, limite + 1, 2))

# # Iterar a través de los números pares
# for numero in iterador_pares:
#     print(numero)

# ¿Qué es un generador y cómo se utiliza?

# Un generador es una función que produce una secuencia de valores sobre los cuales se puede iterar, usando la palabra clave yield en lugar de return. Aquí hay un ejemplo básico:

# def mi_generador():
#     yield 1
#     yield 2
#     yield 3

# # Usar el generador
# for valor in mi_generador():
#     print(valor)

# ¿Cómo crear un generador para la serie de Fibonacci?

# La serie de Fibonacci es una secuencia donde cada número es la suma de los dos anteriores. Podemos crear un generador para producir esta serie:

# def fibonacci(limite):
#     a, b = 0, 1
#     while a < limite:
#         yield a
#         a, b = b, a + b

# # Usar el generador para la serie de Fibonacci hasta 10
# for numero in fibonacci(10):
#     print(numero)

# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))

# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)


# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)