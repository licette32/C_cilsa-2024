# 1- modo apertura: r, w, a
# 2- nombre archivo: notas.txt, /python/notas.txt


# 1 - Abrir un archivo

# opcion 1: una manera tradicional. open, close
# opcion 2: moderna. open, with as

with open("notas.txt", "r") as archivo:
    contenido = archivo.readline()
    print(contenido)

# 2 - Leer un archivo
"""
    read, readline, readlines
"""
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

# 3- Escribir en un archivo
"""
    sobreescribir -> w (si no existe, lo crea)
    añadir        -> a
"""

with open("nuevo_archivo.txt", "w") as archivo:
    archivo.write("Hola buenas tardes\n")
    archivo.write("Adios hasta el proximo jueves!\n")

with open("nuevo_archivo.txt", "a") as archivo:
    archivo.write("David Huertas")

# \n = salto de linea