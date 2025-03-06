# Desarrollar un programa que tenga un diccionario con nombres, apellidos y DNIs.
# A continuación, se deberá ingresar 3 personas con los datos y al final informar su contenido por cada persona.


def registrar_personas():
    personas = {}  # Diccionario para almacenar los datos de las personas
    
    # Pedir datos de 3 personas
    for i in range(3):
        print(f"\nIngresar datos para la persona #{i + 1}:")
        
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        
        # Validar que el DNI sea numérico y mayor a 0
        while True:
            dni = input("DNI: ").strip()
            if dni.isdigit() and int(dni) > 0:
                dni = int(dni)
                break
            print("El DNI debe ser un número válido mayor a 0. Intente nuevamente.")
        
        # Crear un diccionario con los datos de la persona
        personas[i + 1] = {"nombre": nombre, "apellido": apellido, "dni": dni}
    
    # Mostrar los datos ingresados
    print("\nDatos ingresados:")
    for clave, datos in personas.items():
        print(f"Persona #{clave}: Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, DNI: {datos['dni']}")
    
    # Mostrar personas con DNI mayor a 40 millones
    mayores_40m = {k: v for k, v in personas.items() if v['dni'] > 40000000}
    
    print("\nPersonas con DNI mayor a 40 millones:")
    for clave, datos in mayores_40m.items():
        print(f"Persona #{clave}: Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, DNI: {datos['dni']}")
    print(f"\nTotal: {len(mayores_40m)}")
    
    print("\nGracias por utilizar nuestro sistema.")

# Ejecutar la función
registrar_personas()