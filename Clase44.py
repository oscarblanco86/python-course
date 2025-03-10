# Resumen
# ¿Cómo funcionan los decoradores en Python?

# Los decoradores en Python son una herramienta poderosa que permite modificar o extender el comportamiento de las funciones o métodos, sin alterar su código original. Este enfoque es especialmente útil en un entorno profesional donde a menudo se desea añadir comportamientos antes o después de la ejecución de una función principal.
# ¿Cuál es la estructura básica de un decorador en Python?

# Un decorador en Python empieza al crear una función que actúa sobre otra función. Este proceso involucra:

#     Una función primaria que realiza una tarea básica, como imprimir un mensaje o realizar una transacción.
#     Un decorador que recibe esta función como argumento, ejecuta código antes y/o después de la función y retorna la función modificada.

# Por ejemplo, consideremos un decorador básico que imprime mensajes antes y después de una función:

# def mi_funcion(parametro):
#     print(f"Procesando: {parametro}")

# def mi_decorador(func):
#     def wrapper(*args, **kwargs):
#         print("Antes de ejecutar la función...")
#         resultado = func(*args, **kwargs)
#         print("Después de ejecutar la función...")
#         return resultado
#     return wrapper

# # Aplicar el decorador
# @mi_decorador
# def procesar_pago():
#     print("Procesando pago...")

# procesar_pago()

# ¿Cómo aplicamos un decorador en un ejemplo práctico?

# Para entender mejor los decoradores, consideraremos un ejemplo donde se añade funcionalidad antes y después de una función que procesa un pago:

#     Se define la función básica procesar_pago:

#     def procesar_pago():
#         print("Procesando pago...")

#     Se crea un decorador que añade logs antes y después de ejecutar la función:

#     def log_decorator(func):
#         def wrapper():
#             print("Iniciando log de la transacción...")
#             func()
#             print("Log de la transacción terminado.")
#         return wrapper

#     Se aplica el decorador usando el símbolo @ y se ejecuta la función:

#     @log_decorator
#     def procesar_pago():
#         print("Procesando pago...")

#     procesar_pago()

# ¿Cómo manejamos permisos con decoradores?

# Los decoradores también pueden ser útiles para verificar permisos antes de ejecutar funciones. Supongamos que deseamos controlar el acceso a una funcionalidad que elimina empleados, solo permitiendo la acción a administradores:

#     Se define una función que elimina un empleado, basándose en un diccionario de datos:

#     def eliminar_empleado(empleado):
#         print(f"Empleado {empleado['nombre']} ha sido eliminado.")

#     Se crea un decorador para verificar el rol del empleado:

#     def verificar_acceso(func):
#         def wrapper(empleado):
#             if empleado.get('role') == 'admin':
#                 return func(empleado)
#             else:
#                 print("Acceso denegado: solo los administradores pueden acceder.")
#         return wrapper

#     Se aplica el decorador y se prueba con distintos roles:

#     @verificar_acceso
#     def eliminar_empleado(empleado):
#         print(f"Empleado {empleado['nombre']} ha sido eliminado.")

#     admin = {'nombre': 'Carlos', 'role': 'admin'}
#     empleado = {'nombre': 'Ana', 'role': 'empleado'}

#     eliminar_empleado(admin)
#     eliminar_empleado(empleado)

# Este ejemplo práctico muestra cómo se puede controlar qué acciones están permitidas para quién, lo que es esencial en entornos colaborativos y de seguridad.
# ¿Qué proponemos como práctica para mejorar en decoradores?

# Como reto adicional, intenta implementar un decorador que registre todas las acciones realizadas por un empleado en un archivo de texto. Esto no solo te ayudará a consolidar el uso de decoradores, sino que también fomentará la reutilización y extensión de funcionalidades en tu código.

# Continuarás aprendiendo sobre decoradores y sus usos avanzados, como incluir parámetros y anidar múltiples decoradores. ¡Sigue adelante en tu viaje de aprendizaje en programación!

def check_access(func):
    def wrapper(employee):
        """
        Check role 'admin
        """
        if employee.get('role') =='admin':
            return func(employee)
        else:
            print('Access denied')
    return wrapper

@check_access
def delete_employee(employee):
    """
    Deleteing employee
    """
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin)
# delete_employee(employee)
