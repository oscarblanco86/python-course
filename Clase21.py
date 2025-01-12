# Resumen

# La recursividad es una técnica fundamental en programación donde una función se llama a sí misma para resolver problemas complejos de manera más sencilla y estructurada.
# ¿Cómo se aplica la recursividad en el cálculo del factorial?

# La recursividad se entiende mejor con ejemplos prácticos. El factorial de un número se define como el producto de todos los números desde ese número hasta 1. Por ejemplo, el factorial de 5 (5!) es 5 * 4 * 3 * 2 * 1.

# En código Python, la función factorial se puede definir recursivamente de la siguiente manera:

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# Este código sigue dos casos clave en la recursividad:

#     Caso base: cuando n es 0, la función retorna 1.
#     Caso recursivo: cuando n es mayor que 0, la función retorna n multiplicado por el factorial de n-1.

# ¿Cómo funciona la recursividad en la serie de Fibonacci?

# La serie de Fibonacci es otra aplicación clásica de la recursividad. En esta serie, cada número es la suma de los dos anteriores, comenzando con 0 y 1. La fórmula es:

# [ F(n) = F(n-1) + F(n-2) ]

# El código Python para calcular el número n-ésimo en la serie de Fibonacci usando recursividad es el siguiente:

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# Aquí también se siguen dos casos:

#     Caso base: cuando n es 0 o 1, la función retorna n.
#     Caso recursivo: para otros valores de n, la función retorna la suma de fibonacci(n-1) y fibonacci(n-2).

def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función
result = sum_numbers(5)
print(f"Suma de los primeros 5 números es: {result}")
