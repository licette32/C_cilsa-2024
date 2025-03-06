class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass
    

class Perro(Animal):
    def __init__(self, nombre, tiene_cola):
        super().__init__(nombre)
        self.tiene_cola = tiene_cola


    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    

mi_perro = Perro("Perrito")
print(mi_perro.hacer_sonido())

mi_gato = Gato("Gatito") # Instanciando la clase
print(mi_gato.hacer_sonido())