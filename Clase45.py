# ¿Qué son los decoradores anidados y cómo se utilizan en Python?

# Los decoradores anidados son una técnica avanzada en Python que permite aplicar múltiples decoradores a una sola función. Son herramientas poderosas que facilitan la modificación del comportamiento de las funciones de manera dinámica y reutilizable. Esta capacidad de anidar decoradores y hacer uso de parámetros adicionales es especialmente útil en proyectos grandes y complejos que requieren control sobre el flujo de ejecución.
# ¿Cómo se crean decoradores anidados?

# Para crear decoradores anidados, es esencial seguir un orden lógico en su construcción:

#     Primero, define el decorador que se llamará inicialmente en el código.
#     Luego, crea el decorador que será invocado por el primero.

# Por ejemplo, en este escenario, queremos simular que un empleado intenta eliminar a otro, y solo los administradores tienen permiso para esa acción. Aquí está el paso a paso para crear ambos decoradores:
# Implementación del decorador 'Check Access'

# Este decorador se asegura de que solo los usuarios con rol de administrador puedan realizar la acción:

# def CheckAccess(role_required):
#     def decorator(func):
#         def wrapper(employee):
#             # Comprueba si el rol del empleado coincide con el requerido
#             if employee['role'] == role_required:
#                 return func(employee)
#             else:
#                 print(f"Acceso denegado. Solo {role_required}s pueden realizar esta acción.")
#         return wrapper
#     return decorator

# Implementación del decorador 'Log Action'

# Este decorador se encarga de registrar cada acción realizada por el usuario:

# def LogAction(func):
#     def wrapper(employee):
#         print(f"Registrando acción para el empleado {employee['nombre']}.")
#         func(employee)
#     return wrapper

# Aplicación de los decoradores en una función

# Con ambos decoradores definidos, podemos aplicarlos a una función que elimina a un empleado:

# @CheckAccess('admin')
# @LogAction
# def eliminar_empleado(employee):
#     print(f"El empleado {employee['nombre']} ha sido eliminado.")

# ¿Cómo funcionan juntos los decoradores?

# Estos decoradores, cuando se aplican en conjunto a una función, se ejecutan en el orden en que están colocados, comenzando por el decorador más interno. Así, en el ejemplo anterior, LogAction se ejecutará antes que CheckAccess en el contexto de la función eliminar_empleado.

#     Primero, LogAction registrará la acción independientemente del rol del empleado.
#     Luego, CheckAccess verificará si el empleado tiene el rol necesario antes de permitir la eliminación.

# Beneficios de usar decoradores anidados

#     Modularidad: Permiten aislar funcionalidades como la verificación de permisos y el registro de acciones, lo que hace que el código sea más limpio y fácil de mantener.
#     Reutilizabilidad: Puedes reutilizar los decoradores con diferentes funciones, ajustándolos con parámetros para casos específicos.
#     Flexibilidad: La capacidad de pasar parámetros a los decoradores permite una personalización extrema para adaptarse a las neces

#     idades específicas de las aplicaciones.

# Dominar el uso de decoradores anidados te permitirá escribir código Python más eficiente y limpio, mejorando así tu productividad como desarrollador. ¡Sigue practicando y verás cómo estas habilidades se vuelven indispensables en tu carrera profesional!
# Lecturas recomendadas



#Decorador que comprueba si un empleado tiene un rol especifico

def check_access(required_role):
    """
    Check role
    """
    def decorator(func):
        """
        receives a function
        """
        def wrapper(employee):
            """
            Check if eployee role matches the required role
            """
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'Access denied. Only {required_role} can access')
        return wrapper
    return decorator

def log_action(func):
    """
    docstring
    """
    def wrapper(employee):
        print(f'Registrando accion para el emplreado {employee['name']}')
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

# delete_employee(admin)
delete_employee(employee)