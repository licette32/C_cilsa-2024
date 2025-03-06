# Programa

try:
    num_1 = float(input("Ingresar el primer número: "))
    num_2 = float(input("Ingresar el segundo número: "))
    
    resultado = num_1 / num_2 # Realizar la división
    
    print(f"El resultado de la división es: {resultado}")
    
except ValueError:
    print("Error: Debes ingresar números válidos.") # Manejar el error si no se ingresan números
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.") # Manejar el error si se intenta dividir por cero
