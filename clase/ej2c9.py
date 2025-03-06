# Datos de las 4 personas en forma de diccionarios
personas = [
    {"nombre": "Anibal", "apellido": "Pérez", "edad": 30},
    {"nombre": "María", "apellido": "Gómez", "edad": 25},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 40},
    {"nombre": "Kevin", "apellido": "Sánchez", "edad": 35}
]

# Nombre del archivo de salida
archivo_salida = "datos_personas.txt"

# Abrir el archivo en modo escritura
with open(archivo_salida, "w") as archivo:
    # Recorrer la lista de personas y escribir sus datos en el archivo
    for persona in personas:
        archivo.write(f"Nombre: {persona['nombre']}\n")
        archivo.write(f"Apellido: {persona['apellido']}\n")
        archivo.write(f"Edad: {persona['edad']}\n")
        archivo.write("\n")  # Separador entre personas

print(f"Datos de las personas guardados en {archivo_salida}")