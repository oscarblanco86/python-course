# ¿Qué es un tipo de dato en Python?

# En Python, un tipo de dato se refiere a la clase de datos que una variable puede contener. Esto se puede verificar con la función type(), que devuelve la clase del valor contenido en la variable. Por ejemplo, type('Hello') devuelve class 'str', indicando que el dato es una cadena de texto.
# ¿Cómo se manejan los números enteros en Python?

# Los números enteros en Python pertenecen a la clase int, que se utiliza para representar números sin parte decimal. Al declarar una variable como x = 5, se puede comprobar su tipo con type(x), que devolverá int. Esta clase es ideal para operaciones aritméticas básicas.
# ¿Qué son los números flotantes y cómo se usan?

# Los números flotantes pertenecen a la clase float y se utilizan para representar números con decimales. Por ejemplo, y = 5.0 es un número flotante. Para operaciones con números muy grandes o pequeños, se puede usar la notación científica, como z = 1e6, que representa 1 multiplicado por 10 elevado a 6. Python maneja automáticamente las operaciones aritméticas con flotantes devolviendo resultados en float.
# ¿Cómo se utiliza la notación científica en Python?

# La notación científica se emplea para representar números muy grandes o muy pequeños de manera compacta. Por ejemplo, 1e6 representa 1,000,000 y 1e-6 representa 0.000001. Esta notación es útil en cálculos científicos y financieros, donde los números pueden variar significativamente en magnitud.
# ¿Cómo se manejan los booleanos en Python?

# Los booleanos en Python pertenecen a la clase bool y pueden tomar uno de dos valores: True o False. Estos valores son fundamentales para las operaciones lógicas y las estructuras de control de flujo, como las condicionales. Al declarar una variable como isTrue = True, se puede comprobar su tipo con type(isTrue), que devolverá bool.
# ¿Qué importancia tienen los tipos de datos en las operaciones matemáticas?

# Es crucial entender los tipos de datos al realizar operaciones matemáticas en Python. Las operaciones entre enteros (int) y flotantes (float) devuelven resultados en float. Por ejemplo, sumar un entero y un flotante, como x + y, devolverá un resultado en float. Este comportamiento es importante para evitar errores cuando el usuario ingresa un tipo de dato inesperado.
# ¿Cómo se usan los comentarios en Python?

# Los comentarios en Python se crean utilizando el símbolo #, y se usan para anotar y explicar el código. Las líneas comentadas no son ejecutadas por Python. Por ejemplo, # Este es un comentario es una línea que Python ignora durante la ejecución.
# ¿Qué operaciones matemáticas básicas se pueden hacer en Python?

# En Python se pueden realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Por ejemplo, se puede sumar dos variables x e y con x + y. Si se utilizan dos números flotantes, el resultado será también un número flotante.

x = 10
y = 5.678
#z = 1.2E6
#a = 1.2E-6
print(type(x))
print(type(y))
#print(z)
#print(a)
print(x + x)
print(x + y)
print(y + y)
is_true = True
is_false = False
print(is_true)
print(type(is_true))