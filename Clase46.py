# Resumen
# ¿Cómo funcionan los decoradores en la programación orientada a objetos?

# Los decoradores en Python son un elemento poderoso que añade funcionalidad adicional a métodos o funciones sin modificar su estructura interna. Este concepto es bien conocido en el contexto de funciones, pero su aplicación en la programación orientada a objetos (POO) expande aún más sus posibilidades. Aquí exploramos su uso dentro de clases.
# ¿Qué es un método estático?

# Los métodos estáticos no dependen de la instancia de la clase sino que pertenecen a la clase en sí. Se utiliza el decorador @staticmethod cuando se desea crear un método que no necesita acceder a la clase o modificar sus datos.

# class Calculadora:
#     @staticmethod
#     def suma(a: int, b: int) -> int:
#         return a + b

#     Ventaja: Ideal para operaciones que no requieren acceso a las propiedades o métodos de clase.

# ¿Qué hace un método de clase?

# Un método de clase está vinculado a la clase y no a la instancia. Utiliza el decorador @classmethod, y el primer parámetro siempre es cls, que representa la clase.

# class Contador:
#     cuenta = 0

#     @classmethod
#     def incrementar(cls):
#         cls.cuenta += 1

#     Uso común: Modificar el estado de clase común a todas las instancias.

# ¿Cómo se utiliza el decorador property?

# El decorador property permite acceder a un método como si fuese un atributo. Esto mejora la encapsulación y mantiene el control sobre cómo se manipula la información interna de la clase.
# Ejemplo de clase Círculo

# class Circulo:
#     def __init__(self, radio: float):
#         self._radio = radio
    
#     @property
#     def area(self) -> float:
#         return 3.1416 * self._radio ** 2
    
#     @property
#     def radio(self) -> float:
#         return self._radio

#     @radio.setter
#     def radio(self, valor: float):
#         if valor < 0:
#             raise ValueError("El radio no puede ser negativo")
#         self._radio = valor

# ¿Por qué usar property?

#     Control del acceso: El acceso a atributos sensibles puede ser controlado sin afectar la interfaz externa.

#     Flexibilidad: Los atributos pueden ser modificables, lo que permite agregar lógica para validaciones o cálculos al cambiar valores.

#     Encapsulación: Permite ocultar la lógica de cálculo o validaciones, entregando una interfaz limpia al usuario de la clase.

# Reflexiones finales sobre decoradores en POO

# Los decoradores como staticmethod, classmethod, y property son herramientas valiosas que enriquecen el diseño de clases en Python. Permiten:

#     Añadir funcionalidad especial sin modificar el código base.
#     Mejorar la legibilidad y profesionalidad del código.
#     Mantener un diseño orientado a objetos disciplinado y eficiente.

# # ¡Ahora depende de ti aplicarlos y descubrir todo su potencial en tus proyectos! Recuerda: ¡Un gran poder conlleva una gran responsabilidad en el código!



# class method

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count +=1

Counter.increment()
Counter.increment()
print(Counter.count)

# static method

class Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b