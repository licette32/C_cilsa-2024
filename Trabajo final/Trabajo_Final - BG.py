import csv
import os

def leer_csv(nombre_archivo): # Se lee el archivo
    try:
        with open(nombre_archivo, mode='r', encoding='latin-1') as archivo: 
            lector = csv.DictReader(archivo)
            return [fila for fila in lector], lector.fieldnames
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        exit()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit()

def filtrar_por_edad(datos, edad_minima, edad_maxima):
    """Como primer punto filtraremos una lista de diccionarios según el rango de edades"""
    return [
        persona for persona in datos
        if edad_minima <= int(persona["Edad"]) <= edad_maxima
    ]

def filtrar_por_columna(datos, columna, valor):
    return [persona for persona in datos if persona[columna].lower() == valor.lower()]

def guardar_csv(nombre_archivo, datos, campos):
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos)
            print(f"Los datos se guardaron exitosamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        exit()

def mostrar_menu():
    """Menú de opciones para el usuario."""
    print("\nOpciones:")
    print("1. Filtrar por rango de edades")
    print("2. Filtrar por nombre")
    print("3. Filtrar por ciudad")
    print("4. Salir")

def main():
    archivo_origen = 'C:/Users/bever/Documents/cilsa python/datos.csv'
    
    """Verifico si existe el archivo antes de intentar leerlo"""
    if not os.path.exists(archivo_origen):
        print(f"Error: El archivo '{archivo_origen}' no existe. Verifica la ruta.")
        return

    datos, campos = leer_csv(archivo_origen)
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            # 1- sección donde se filtra por rango de edades
            try:
                edad_minima = int(input("Edad mínima: "))
                edad_maxima = int(input("Edad máxima: "))
            except ValueError:
                print("Error: Las edades deben ser números enteros.")
                continue

            datos_filtrados = filtrar_por_edad(datos, edad_minima, edad_maxima)
            if datos_filtrados:
                print("\nResultados:")
                for persona in datos_filtrados:
                    print(persona)
                guardar = input("\n¿Deseas guardar los resultados en un archivo? (s/n): ").lower()
                if guardar == 's':
                    archivo_guardado = 'resultados_filtrados.csv'
                    guardar_csv(archivo_guardado, datos_filtrados, campos)
                    print(f"Los resultados se guardaron correctamente en '{archivo_guardado}'.")
                else:
                    print("Resultados no guardados.")
            else:
                print("No se encontraron resultados en ese rango de edades.")

        elif opcion == '2':
            # 2- Seccción donde filtramos por nombre
            nombre = input("Ingresa el nombre a buscar: ")
            datos_filtrados = filtrar_por_columna(datos, "Nombre", nombre)
            if datos_filtrados:
                print("\nResultados:")
                for persona in datos_filtrados:
                    print(persona)
                guardar = input("\n¿Deseas guardar los resultados en un archivo? (s/n): ").lower()
                if guardar == 's':
                    archivo_guardado = 'resultados_filtrados.csv'
                    guardar_csv(archivo_guardado, datos_filtrados, campos)
                    print(f"Los resultados se guardaron correctamente en '{archivo_guardado}'.")
                else:
                    print("Resultados no guardados.")
            else:
                print("No se encontraron resultados para ese nombre.")

        elif opcion == '3':
            # 3- Sección donde filtramos por ciudad
            ciudad = input("Ingresa la ciudad a buscar: ")
            datos_filtrados = filtrar_por_columna(datos, "Ciudad", ciudad)
            if datos_filtrados:
                print("\nResultados:")
                for persona in datos_filtrados:
                    print(persona)
                guardar = input("\n¿Deseas guardar los resultados en un archivo? (s/n): ").lower()
                if guardar == 's':
                    archivo_guardado = 'resultados_filtrados.csv'
                    guardar_csv(archivo_guardado, datos_filtrados, campos)
                    print(f"Los resultados se guardaron correctamente en '{archivo_guardado}'.")
                else:
                    print("Resultados no guardados.")
            else:
                print("No se encontraron resultados para esa ciudad.")

        elif opcion == '4': # Sección de salida del programa
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
