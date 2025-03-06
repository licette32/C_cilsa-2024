import csv

# Nombre del archivo CSV
archivo_csv = "datos.csv"

# Ciudad a buscar (poner las letras en minúsculas)
ciudad_a_buscar = input("Ingrese la ciudad para filtrar: ").lower()

# Lista para almacenar las filas que coinciden con la ciudad
filas_coincidentes = []

# Leer el archivo CSV y filtrar por ciudad
with open(archivo_csv, 'r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        # recupero la ciudad de cada persona (en minúscula)
        ciudad = fila['Ciudad'].lower()
        if ciudad == ciudad_a_buscar:
            # Si la ciudad de la fila actual coincide con la ciudad buscada,
            # entonces guardo la fila entera en la lista "filas_coincidentes".
            filas_coincidentes.append(fila)

# Mostrar las filas coincidentes
if filas_coincidentes:
    print(f"Personas en la ciudad de {ciudad_a_buscar.capitalize()}:")
    for fila in filas_coincidentes:
        print(f"Nombre: {fila['Nombre']}, Edad: {fila['Edad']}, Ciudad: {fila['Ciudad']}")
else:
    print(f"No se encontraron personas en la ciudad de {ciudad_a_buscar.capitalize()}.")