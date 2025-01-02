# Resumen

# En programación, las estructuras condicionales son esenciales para tomar decisiones basadas en ciertas condiciones. Por ejemplo, al usar la instrucción IF en Python, se puede verificar si una variable cumple con una condición específica y ejecutar el código correspondiente.
# ¿Cómo se usa la estructura IF en Python?

# Para utilizar el IF, primero se define una variable, por ejemplo, x = 10. Luego, se escribe la estructura condicional usando la palabra reservada IF seguida de la condición, como if x > 5:. Si esta condición es verdadera, se ejecuta el código dentro del IF, que debe estar indentado.

# x = 10
# if x > 5:
#     print("x es mayor que 5")

# ¿Qué pasa si la condición del IF es falsa?

# Si la condición del IF no se cumple, se puede utilizar la instrucción else para manejar el caso contrario. Por ejemplo, si x es menor o igual a 5, se ejecutará el bloque de código dentro del else.

# x = 3
# if x > 5:
#     print("x es mayor que 5")
# else:
#     print("x es menor o igual a 5")

# ¿Cómo se manejan múltiples condiciones?

# Cuando hay múltiples condiciones, se puede usar elif (else if). Esto permite agregar condiciones adicionales entre if y else.

# x = 5
# if x > 5:
#     print("x es mayor que 5")
# elif x == 5:
#     print("x es igual a 5")
# else:
#     print("x es menor que 5")

# ¿Cómo se manejan múltiples condiciones en un solo IF?

# Para evaluar múltiples condiciones en una sola sentencia IF, se pueden utilizar los operadores lógicos and y or. El operador and requiere que ambas condiciones sean verdaderas, mientras que el operador or requiere que al menos una condición sea verdadera.

# x = 15
# y = 30
# if x > 10 and y > 25:
#     print("x es mayor que 10 y y es mayor que 25")
# if x > 10 or y > 35:
#     print("x es mayor que 10 o y es mayor que 35")

# ¿Qué es la negación en las condiciones?

# La palabra reservada not se utiliza para negar una condición. Si una condición es verdadera, not la convierte en falsa, y viceversa.

# x = 15
# if not x > 20:
#     print("x no es mayor que 20")

# ¿Cómo se anidan las estructuras IF?

# Los IF anidados permiten evaluar condiciones dentro de otras condiciones. Esto es útil para verificar múltiples niveles de requisitos.

# isMember = True
# age = 15
# if isMember:
#     if age >= 15:
#         print("Tienes acceso ya que eres miembro y mayor que 15")
#     else:
#         print("No tienes acceso ya que eres miembro, pero menor a 15 años")
# else:
#     print("No eres miembro y no tienes acceso")



# if_ejercicio_1.py

x = 5
if x > 5:
    print("X es mayor que 5")
elif x == 5:
    print("X es igual que 5")
else:
    print("X es menor que 5")
print("afuera")

# if_ejercicio_2.py

x = 15
y = 20

if x>10 and y>25:
    print("X es mayor que 10 y Y es mayor que 15")

if x>10 or y>25:
    print("X es mayor que 10 O Y es Mayor que 25")

if not x>10:
    print("X no es mayor que 10")

# if_ejercicio_3.py

is_member = True
age = 11

if is_member:
    if age>=15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 aÃ±os")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 aÃ±os")
else:
    print("No eres miembro y NO TIENES ACCESO")
