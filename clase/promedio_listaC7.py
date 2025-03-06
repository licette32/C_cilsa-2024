numeros = [10, 40, 50, 90]

total = 0
for numero in numeros: # lista, string
    total += numero

promedio = total / len(numeros)
print(promedio)

# mas cosas....

# nueva lista --> calcular el promedio

# nueva lista --> ....

# Para calcular el promedio de cada lista nueva que aparezca,
# debo escribir desde la linea 3 hasta la 8, varias veces en todo mi programa
# NO SE DEBE HACER ESTO --> solucion: funcion.


# SOLUCION USANDO FUNCION
def calcular_promedio(numeros):
    # total = 0
    # for numero in numeros:
    #     total += numero

    # promedio = total / len(numeros)
    total = sum(numeros)
    return total / len(numeros)


numeros = [10, 40, 50, 90]
# calcular el promedio
promedio = calcular_promedio(numeros)
# mostrar el resultado
print(promedio)

# AHORA solamente necesito invocar a mi funcion con una linea de codigo,
# cada vez que necesito calcular el promedio
lista2 = [10, 400, 50, 90]
lista3= [100, 40, 50, 90]

promedio2 = calcular_promedio(lista2)
promedio3 = calcular_promedio(lista3)


# Ej: calcular el area de un rectangulo

# definir mi funcion
def calcular_area(base, altura):
    return base * altura


# probar el comportamiento de mi funcion
print(calcular_area(5, 10))
print(calcular_area(9, 30))
print(calcular_area(9, "d"))

# parametros opcionales: base=10
# no se cuantos valores voy a enviar a una funcion: * **
