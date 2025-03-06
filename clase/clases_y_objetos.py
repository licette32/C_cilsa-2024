"""
 POO: Es un paradigma de programacion que organiza 
 el todo (software) en objetos.

 Clase: plantilla base.

 Objeto: instancia de esa clase.

 Conceptos relacionados: Encapsulamiento, Herencia, 
 Polimorfismo y Abstracción.

"""

"""
Python: 
- Definicion de clases
- Herencia
- Metodos y atributos
- Constructores
- Encapsulamiento y polimorfismo.
"""


class Gato:
    # va a tener atributos: edad, nombre, color
    # metodos: acciones que puede hacer un gato (clase)
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Miau"

class Perro:
    # va a tener atributos: edad, nombre, color
    # metodos: acciones que puede hacer un gato (clase)
    
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Guau"

mi_gato = Gato("Gatito") # Instanciando la clase
print(mi_gato.hacer_sonido())

mi_perro = Perro("Firulais")
print(mi_perro.hacer_sonido())
