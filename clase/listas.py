# Creación de una lista
mi_lista = [1, 2, 3, 4, 5]


# Acceder a elementos de la lista por índice
print("Primer elemento:", mi_lista[0])
print("Último elemento:", mi_lista[-1]) # funciona? que devuelve? y si coloco -2?

# No puedo acceder con indices fuera del rango de la lista
# print("Elemento:", mi_lista[6])

# Modificación de elementos de la lista
mi_lista[0] = 10
print("Lista modificada:", mi_lista)


# Agregar elementos a la lista
mi_lista.append(6)
print("Lista con elemento agregado:", mi_lista)

# Eliminar elementos de la lista
elemento_eliminado = mi_lista.pop(2)
print("Elemento eliminado:", elemento_eliminado)
