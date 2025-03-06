# Solicitar ingresar un nombre 5 veces y guardarlos en una lista. Luego mostrarlos.

nombres = []
for i in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

for nombre in nombres:
    print(f"El nombre ingresado fue: {nombre}")



# Solicitar ingresar un nombre 5 veces y guardarlos en una lista. Luego mostrarlos. Termina el programa si el usuario ingresa la palabra "SALIR" en mayuscula.-

lista_nombres = []
cantidad = 0
while cantidad<5:
    nombre = input("Ingrese un nombre (o ingrese SALIR para salir): ")
    if nombre == "SALIR":
        break
    lista_nombres.append(nombre)
    cantidad+=1

for nombre in lista_nombres:
    print(nombre)
