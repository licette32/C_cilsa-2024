# Este archivo contiene conceptos y operaciones básicas sobre diccionarios.

# Declaración de diferentes tipos de colecciones en Python
# listas --> mi_lista = [1, 2, 3]
# tuplas --> mi_tupla = (1, 2, 3)
# conjuntos --> mi_conjunto = {1, 2, 3}
# diccionarios --> mi_diccionario = dict() o {}

# Diccionario de ejemplo
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Accediendo a valores en un diccionario
print(diccionario['a'])  # Muestra el valor asociado a la clave 'a'
# Si intentas acceder a una clave inexistente de esta forma, obtendrás un error:
# print(diccionario['m'])
# Es mejor usar el método `get` para evitar errores:
print(diccionario.get('m', "Esta clave no existe."))

# Modificar un valor en un diccionario
diccionario['b'] = 20
print(diccionario['b'])  # Ahora el valor de 'b' es 20

# Añadir una nueva clave-valor
diccionario['d'] = 4
print(diccionario)

# Eliminar una clave-valor
del diccionario['b']
print(diccionario)

# Métodos útiles en diccionarios
diccionario = {'a': 1, 'b': 2, 'c': 3}
print(diccionario.keys())   # Muestra todas las claves
print(diccionario.values()) # Muestra todos los valores
print(diccionario.items())  # Muestra pares clave-valor

# Iterar sobre un diccionario
for clave, valor in diccionario.items():
    print(clave, valor)

# Eliminar todos los elementos del diccionario
# diccionario.clear()
