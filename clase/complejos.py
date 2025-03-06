# TUPLAS = "tuple"
# inmutable = no puede cambiar sus valores luego de crearlo
# indice = posicion = numero --> acceder a los elementos
mi_tupla = ('Damian', 29)
print(mi_tupla[0])

tupla_vacia = tuple()
print(type(tupla_vacia))

# Conjuntos
# conjunto = en ingles "set"
# no ordenadas, elementos unicos = no guarda elementos repetidos

mi_conjunto = {3, 4.12, 'Juan'}
conjunto_vacio = set() # {} --> diccionario X

print(type(conjunto_vacio))

# Métodos

# agregar
conjunto_vacio.add(5)



# Listas
# list en ingles.
# flexibles = casi ninguna restriccion

mi_lista = ["Gaston", 30, 35444555]

print(mi_lista[1])
mi_lista.append(90)
mi_lista.append("Perez")

# ["Gaston", 30, 35444555, 90, "Perez"]
print(mi_lista[4])
print(mi_lista)

# mostrar los datos de la lista: for sobre la lista

texto = ""
for elemento in mi_lista:
    # texto: agregar mas texto... 
    print(elemento)

# append(elemento), insert(indice, elemento)
# remove(elemento)
# sort()

# lista.append(elemento)



# DICCIONARIOS
# ingles --> dict
# no manejan indices

mi_diccionario = {} # dict()

# clave-valor = pares clave-valor = registro
numeros = {
    1: 'Uno', 
    2: 'Dos'
}

print(numeros[2])