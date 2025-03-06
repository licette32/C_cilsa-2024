# Crear una lista vacía para almacenar las calificaciones
lista_calif = []

while True:
    nota = int(input("Introduzca la nota del examen: ")) # Pedir al usuario que introduzca una calificación
    
    if nota == 0: 
        break # Finalizar la carga de datos
    else:
        lista_calif.append(nota) # Agregar la calificación a la lista


if lista_calif:
    print("\nCalificaciones ingresadas:") # Mostrar todas las calificaciones ingresadas
    for i, nota in enumerate(lista_calif, start=1):
        print(f"Calificación {i}: {nota}")
else:
    print("No se ingresaron calificaciones.")
