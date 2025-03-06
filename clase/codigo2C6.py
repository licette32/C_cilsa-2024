# DICCIONARIO SE COMPONE DE CLAVE-VALOR (KEY-VALUE EN INGLES)
mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30, 
    'ciudad': 'Mar del Plata'
    }

# Recorrer el diccionario
print("Claves y valores usando un bucle:")
for clave in mi_diccionario:
    print(f"{clave}: {mi_diccionario[clave]}")

# metodos útiles: keys, values e items.
print(diccionario.keys())   # Muestra todas las claves
print(diccionario.values()) # Muestra todos los valores
print(diccionario.items())  # Muestra pares clave-valor
# Pero devuelve un objeto/estructura que no es iterable.
# Por ejemplo: diccionario.keys() devuelve un objeto de tipo dict_keys con una lista de claves dentro.
# Para navegar sobre ella, podemos usar el for. También podemos convertirlo en otro tipo de dato, por ejemplo, una lista y guardarlo.

# Convertir diccionario a lista
mis_claves = list(mi_diccionario.keys())
print(mis_claves)
print(type(mis_claves))


# Recorrer pares clave-valor con items()
print("\nUsando items() para iterar sobre el diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")


"""
¿Cómo resolver desafío 13?

diccionario = dict()

# Ingresar datos de 3 personas
for i in range(3):
    # realizar lis inputs de nombre, dni, etc.

    nombre= input("Ingrese un nombre: ")
    # lo mismo para los demas datos

    # armar un diccionario con esos datos de ESA PERSONA
    persona = {'nombre': nombre, ... , ...}
    
    # Agregar a la persona dentro de mi diccionario general
    # uso el i para crear claves numericas en mi diccionario (ver el material subido al Moodle sobre Armar Claves)
    diccionario[i+1] = persona

# Finalmente, mostrar el diccionario general

"""
