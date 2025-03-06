# Enunciado: Crear un diccionario para almacenar la información de las personas, el nombre y apellido.



personas = {}

# Pedir al usuario que ingrese el nombre y apellido de 5 personas
for i in range(1, 6):  # Comenzar en 1 para que las claves sean más intuitivas
    nombre = input(f"Ingrese el nombre de la persona {i}: ")
    apellido = input(f"Ingrese el apellido de la persona {i}: ")

    # Agregar la información al diccionario usando la clave correspondiente
    personas[i] = {'nombre': nombre, 'apellido': apellido}

# Mostrar el diccionario con la información de las personas
# Uso del método "items" para iterar sobre cada registro (clave-valor) del diccionario
print("\nInformación de las personas:")
for clave, info in personas.items():
    print(f"Persona {clave}: {info['nombre']} {info['apellido']}")
