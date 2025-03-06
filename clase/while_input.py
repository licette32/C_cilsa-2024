#Sumar números hasta que el usuario ingrese '0' (usando while)

suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))  # Solicita el primer número
while numero != 0:  # Mientras el número no sea 0, sigue sumando
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))
print("La suma total es:", suma)