# TUPLAS
dias = ('Lunes', 'Martes')
dia = dias[1]
# print(dia)

# LISTAS
elementos = ['Diego', 35444222, 1900]
#Agregar un nuevo valor
elementos.append('Díaz')
elementos.insert(1,33999888)
#Eliminar
elementos.remove(1900)
print(elementos)

#CONJUNTOS
conjunto_colores = {"amarillo", "azul", "rosa", "blanco", "rojo"}
if "rojo" in conjunto_colores:
    print("El color 'rojo' está en el conjunto.")
else:
    conjunto_colores.add("rojo")
print(conjunto_colores)

# DICCIONARIO
# Key o clave : Value o valor
dic = {'nombre':'David', 'ciudad':'La Plata'}
variable={}
print(type(variable))