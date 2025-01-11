# Resumen

# En Python, uno de los principios fundamentales es el de divide y vencerás. Esto se refiere a dividir el código en porciones más pequeñas para facilitar su legibilidad, mantenimiento y reutilización. Las funciones nos permiten encapsular lógica específica, evitando la duplicación de código.
# ¿Cómo se definen las funciones en Python?

# Las funciones en Python se definen utilizando la palabra reservada def, seguida del nombre de la función y los parámetros que representan la información necesaria para su ejecución.

# def saludar():
#     print("Hola, mundo")

# saludar()

# ¿Cómo se utilizan los parámetros en una función?

# Podemos agregar parámetros a una función para que reciba información dinámica. Por ejemplo, para saludar a una persona específica:

# def saludar(name):
#     print(f"Hola, {name}")

# saludar("Carla")

# ¿Cómo manejar múltiples parámetros en una función?

# Las funciones pueden tener múltiples parámetros. Por ejemplo, para saludar con nombre y apellido:

# def saludar(name, last_name):
#     print(f"Hola, {name} {last_name}")

# saludar("Diego", "Antezano")

# ¿Qué ocurre si falta un argumento?

# Si no se pasan todos los argumentos, Python generará un error indicando que falta un argumento posicional:

# saludar("Diego")

# ¿Cómo definir valores predeterminados para parámetros?

# Podemos asignar valores predeterminados a los parámetros, que se utilizarán si no se proporciona uno específico:

# def saludar(name, last_name="No tiene apellido"):
#     print(f"Hola, {name} {last_name}")

# saludar("Diego")

# ¿Cómo pasar parámetros por nombre?

# Podemos pasar parámetros por nombre, lo que permite cambiar el orden de los argumentos:

# saludar(last_name="Florida", name="Carla")

# ¿Cómo crear una calculadora con funciones en Python?

# Podemos definir funciones para operaciones básicas y una función principal para manejarlas:

# def suma(a, b):
#     return a + b

# def resta(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     return a / b

# def calculadora():
#     while True:
#         print("Seleccione una operación:")
#         print("1. Suma")
#         print("2. Resta")
#         print("3. Multiplicación")
#         print("4. División")
#         print("5. Salir")
        
#         opcion = int(input("Ingrese su opción: "))
        
#         if opcion == 5:
#             print("Saliendo de la calculadora.")
#             break
        
#         if opcion in [1, 2, 3, 4]:
#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))
            
#             if opcion == 1:
#                 print("La suma es:", suma(num1, num2))
#             elif opcion == 2:
#                 print("La resta es:", resta(num1, num2))
#             elif opcion == 3:
#                 print("La multiplicación es:", multiplicar(num1, num2))
#             elif opcion == 4:
#                 print("La división es:", dividir(num1, num2))
#         else:
#             print("Opción no válida, por favor intente de nuevo.")

# calculadora()

# ¿Qué se debe considerar al crear funciones en Python?

# Es crucial tener en cuenta el tipo de datos que se manejan, validar entradas del usuario y asegurarse de que las funciones se llamen correctamente para evitar errores en la ejecución.

## funciones_calculator.py
def add(a,b):
    return a+b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingrese su opción (1,2,3,4,5): ")

        if option == "5":
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", substract(num1, num2))
            elif option == "3":
                print("La división es:", divide(num1, num2))
            elif option == "4":
                print("La multiplicación es:", multiply(num1, num2))
        
        else:
            print("Opción no válida, por intenta de nuevo")

calculator()        

## funciones.py
def greet(name, last_name="No tiene apellido"):
    print("Hola", name, last_name)

greet("Carli", "Florida")
greet("Diego")
greet(last_name = "Florida", name = "Carli")