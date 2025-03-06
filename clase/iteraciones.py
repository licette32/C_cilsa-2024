# Creación de una lista
mi_lista = [1, 2, 3, 4, 5]




while True:
    ingrediente = input("Ingrediente: ")
    if ingrediente == "Azucar":
        break
    mi_lista.append(ingrediente)




# Iterar sobre los elementos de la lista
print("Elementos de la lista:")

for elemento in mi_lista:
    print(elemento)

# Obtener la longitud de la lista
# funcion: len
print("Longitud de la lista:", len(mi_lista))

# Comprobar si un elemento está en la lista
if 4 in mi_lista:
    print("el 4 está en la lista")
else:
    print("el 4 NO está en la lista")

# Métodos

# Algunos conocidos en listas:
# lista.sort()
# lista.pop()
# lista.reverse()
