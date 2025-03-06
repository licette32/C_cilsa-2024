# ENUNCIADO

# Realizar un programa en el cual se ingresen dos numeros e informe si el primero es múltiplo del segundo.
# En caso contrario deberá generar un mensaje adecuado.


# Primero solicito al usuario que ingrese dos números enteros
numero1 = int(input("Ingresar el primer número entero: "))
numero2 = int(input("Ingresar el segundo número entero: "))

# Se debe tener en cuenta que el segundo numero NO debe ser cero
if numero2 == 0:
    print("El segundo número no puede ser cero porque la división por cero no está definida.")
else:
    # corroboro si el primero número es múltiplo del segundo número
    if numero1 % numero2 == 0:
        print(f"{numero1} es múltiplo de {numero2}.")
    else:
        print(f"{numero1} no es múltiplo de {numero2}.")