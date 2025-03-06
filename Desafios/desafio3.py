# Se solicita ingresar un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    # determino el numero par con el operador %
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    # si el residuo del operador de la división del número ingresado entre 2 nos da cero,
    # entonces será par
    # si el residuo es distinto de cero entonces será impar