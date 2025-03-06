# Sumar números introducidos por el usuario (usando for)

suma = 0
for i in range(5):  # El bucle se ejecuta 5 veces
    numero = int(input("Ingresa un número: "))  # Solicita al usuario un número
    suma += numero
print("La suma de los números es:", suma)