# Crear una lista vacía para almacenar las calificaciones
lista_calif = []

#Introduce las notas del examen (solo entre 6 y 10). Ingresa 0 para finalizar.

while True:
    nota = int(input("Introducir la nota del examen: "))    # Introducir una calificación
    if nota == 0:
        break        # Finalizar la carga de datos
    elif 6 <= nota <= 10:
        lista_calif.append(nota)        # Agregar la calificación a la lista si las notas estan entre 6 y 10
    else:
        print("Nota no permitido. Ingresa una nota entre 6 y 10.")

if lista_calif:
    print("\nCalificaciones válidas ingresadas:") # Mostrar todas las calificaciones ingresadas
    for i, nota in enumerate(lista_calif, start=1):
        print(f"Calificación {i}: {nota}")
else:
    print("No se ingresaron calificaciones válidas.")
