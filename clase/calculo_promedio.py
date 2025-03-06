# Funcion que calcule el promedio de una lista de numeros


# Definir un funcion
def calculo_promedio(lista):
    # utilizo la función "sum" que existe en python
    # recibe un iterable (lista, tupla, por ejemplo), calcula la sumatoria y devuelve el valor
    suma = sum(lista)
    # "len" es otra función que existe en python y me devuelve la longitud de un elemento
    promedio = suma / len(lista) 
    return promedio

# definir la lista
lista_numeros = [8, 9, 11, 20, 33, 49]
resultado = calculo_promedio(lista_numeros)
print(f"El promedio de los numeros de la lista es: {resultado}")
print(lista)