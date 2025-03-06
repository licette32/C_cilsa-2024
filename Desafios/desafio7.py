# Inicializar el número más grande
numero_big = -1

while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:  # Finalizar si se ingresa 0
        break
    
    if numero > numero_big:  # Actualizar el número más grande
        numero_big = numero

# Mostrar el resultado
if numero_big == -1:
    print("No se ingresaron números válidos.")
else:
    print(f"El número más grande ingresado fue: {numero_big}")
