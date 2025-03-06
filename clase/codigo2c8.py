# Volcar una lista a un archivo

# Opcion 1:

lista_nombres = ["Mauro", "Ximena"]

archivo = open("nombres.txt", "w")

for nombre in lista_nombres:
    print(nombre,file=archivo)
    # No tengo problemas si existe algún numero en la lista
    # El print se encarga de volcar todos los datos sin errores.

archivo.close()


# Opcion 2:

lista_nombres = ["Mauro", "Ximena"]

with open("nombres2.txt", "w") as archivo:
    for nombre in lista_nombres:
        archivo.write(nombre + '\n')
        # Problema: si existe algún numero en la lista me da error.
        # si tengo un numero en la lista, tengo que convertirlo a string.