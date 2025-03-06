# Solicitar los datos de la persona y mostrar un mensaje de presentación
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su email: ")

# Mostrar el mensaje de presentación con diferentes métodos de concatenación

# Operador +
print("\nPresentación con operador +:")
print("Nombre: " + nombre + ", Apellido: " + apellido + ", Edad: " + edad + ", Correo: " + correo)

# f-string
print("\nPresentación con f-string:")
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Correo: {correo}")

# Si uso comas
print("\nPresentación con comas:")
print("Nombre:", nombre, "Apellido:", apellido, "Edad:", edad, "Correo:", correo)