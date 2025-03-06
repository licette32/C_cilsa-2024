def mostrar_datos_diccionario(diccionario):
    # Mostramos los datos de las personas ingresadas
    for key, value in diccionario.items():
        print(f"Persona {key}:")
        print(f"Nombre: {value['Nombre']}")
        print(f"Apellido: {value['Apellido']}")
        print(f"DNI: {value['DNI']}")

diccionario_personas = {}

# Ingresamos los datos de 3 personas
for i in range(3):
    print(f"Ingrese los datos de la persona {i + 1}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")

    diccionario_personas[i + 1] = {"Nombre": nombre, "Apellido": apellido, "DNI": dni}

# sigo haciendo otras operaciones

# Invocar a la funcion
mostrar_datos_diccionario(diccionario_personas)

# mas codigo
