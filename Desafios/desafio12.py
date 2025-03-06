# A partir del desafío 9, modificar el programa para que pueda cargar el nombre y la nota de cada alumno, pero usando DICCIONARIOS.
# Luego debo informar el nombre y la nota tanto de los aprobados como de los desaprobados.

# (ejercicio 9: Retomar el ejercicio del desafío anterior pero solo CARGAR en la LISTA aquellas notas que estén entre 6 y 10 (inclusive)
# MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.)


def cargar_notas():
    alumnos = {}  # Diccionario para almacenar nombre y nota de los alumnos
    
    while True:
        # Solicitar nombre del alumno
        nombre = input("Ingrese el nombre del alumno (o escriba 'salir' para finalizar): ")
        if nombre.lower() == "salir":
            break
        
        # Se solicitar nota del alumno
        try:
            nota = float(input(f"Ingrese la nota de {nombre} (entre 1 y 10): "))
            
            if 1 <= nota <= 10:  # Verificamos que la nota esté dentro del rango permitido
                if nota >= 6:  # Solo se guarda en el caso de que la nota sea de 6 a 10
                    alumnos[nombre] = nota
                else:
                    print("Nota menor a 6, no se guarda en la lista.")
            else:
                print("La nota debe estar entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    
    # Mostrar alumnos aprobados
    print("\nListado de alumnos aprobados:")
    for nombre, nota in alumnos.items():
        print(f"{nombre}: {nota} (Aprobado)")
    
    print("\nGracias por utilizar nuestro sistema.")

# Ejecutar la función
cargar_notas()
