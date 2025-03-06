# Validación de entrada de edad.

# Descripción:
# Escribe un programa que solicite al usuario que ingrese su edad y valide la entrada.

# Condiciones:

# Si el usuario ingresa un número válido (entero positivo), mostrar el mensaje: "Tu edad es xxx años."
# Si el usuario ingresa un valor no numérico, mostrar: "Por favor, ingresa un número válido."
# Si el número ingresado es negativo o igual a 0, mostrar: "La edad debe ser un número positivo mayor que cero."
# Extras:

# Al finalizar, siempre mostrar un mensaje como: "Gracias por usar nuestro programa."


try:
    edad = int(input("Por favor, ingresa tu edad: "))
    if edad <= 0:
        print("La edad debe ser un número positivo mayor que cero.")
    else:
        print(f"Tu edad es {edad} años.")
except ValueError:
    print("Por favor, ingresa un número válido.")
finally:
    print("Gracias por usar nuestro programa.")