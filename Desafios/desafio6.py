
# Se inicializa una lista para almacenar los números
lista_num = []

# Solicitar al usuario que ingrese 5 números
for i in range(5):
    numero = float(input(f"Ingresa el número {i+1}: "))
    lista_num.append(numero)

# Calcular el promedio
promedio = sum(lista_num) / len(lista_num)

# Mostrar el resultado del programa
print(f"El promedio de los números que has ingresado es: {promedio:.2f}")
