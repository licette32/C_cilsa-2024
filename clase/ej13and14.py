""" DESAFIO 13

Desarrollar un programa que tenga un diccionario con nombres, apellidos y DNIs.

A continuación, se deberá ingresar 3 personas con los datos y al final informar su contenido por cada persona.
"""


# 1. Creamos un diccionario vacío para almacenar los datos de las personas
personas = {}

# 2. Pedimos al usuario que ingrese los datos para 3 personas
for i in range(3):
    print(f"Ingresar datos para la persona #{i + 1}:")
    
    # 2.1 INPUT del nombre
    nombre = input("Nombre: ").strip()
    
    # 2.2 INPUT del apellido
    apellido = input("Apellido: ").strip()
    
    # 2.3 INPUT del DNI
    dni = input("DNI: ").strip()
    
    # 2.4 Creamos un nuevo diccionario con los datos ingresados
    persona = {"nombre": nombre, "apellido": apellido, "dni": dni}
    
    # 2.5 Agregamos el diccionario de la persona al diccionario general
    personas[i + 1] = persona

# 3. Mostramos los datos ingresados para cada persona ---> mayores a 40 millones
print("\nDatos ingresados:")
for clave, datos in personas.items():
    	print(f"Persona #{clave}: Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, DNI: {datos['dni']}")

#*******************************************************************************
"""DESAFIO 14

Mostrar las personas con dni mayores a 40 millones y cuantos son en total.
El siguiente código se le puede agregar al final del código anterior.
"""

# 4. Mostrar las personas con dni mayores a 40 millones y cuantos son en total.

cant_mayores_40 = 0

print("\nCon dni mayor a 40 millones:")
for clave, datos in personas.items():
	if datos['dni'] > 40000000:
		print(f"Persona #{clave}: Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, DNI: {datos['dni']}")
		cant_mayores_40 += 1
print(f"\nTotal: {cant_mayores_40}")