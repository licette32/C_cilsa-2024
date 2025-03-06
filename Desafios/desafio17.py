# Realizar un programa que escriba los datos de un diccionario en un archivo.
# Los datos a guardar son: nombre, apellido, edad, email.
# El diccionario puede estar creado previamente o pueden generarlo desde el teclado.

# Pueden elegir:
# Un diccionario con datos de una sola persona.
# Un diccionario que contiene datos de varias personas (usando diccionarios o listas)

import json

def ingresar_datos():
    personas = []  # Lista para almacenar los datos de varias personas
    
    while True:
        print("\nIngrese los datos de la persona:")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        
        while True:
            try:
                edad = int(input("Edad: ").strip())
                if edad <= 0:
                    print("La edad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: La edad debe ser un número entero.")
        
        email = input("Email: ").strip()
        
        persona = {"nombre": nombre, "apellido": apellido, "edad": edad, "email": email}
        personas.append(persona)
        
        continuar = input("\n¿Desea agregar otra persona? (s/n): ").strip().lower()
        if continuar != "s":
            break
    
    return personas

def guardar_en_archivo(personas, nombre_archivo="personas.json"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(personas, archivo, indent=4)
    print(f"\nDatos guardados en {nombre_archivo} correctamente.")

# Ejecutar el programa
personas = ingresar_datos()
guardar_en_archivo(personas)
