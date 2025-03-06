# Bloque principal con manejo básico de excepciones
try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except ValueError:
    print("Error: ¡Ingrese un número válido!")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print("¡Operación exitosa!")
finally:
    print("Fin del bloque principal.")