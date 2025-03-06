""" 

FUNCION
= bloque de codigo reutilizable y realiza una tarea específica

"""

# 1- definir una funcion: def saludar(): bloque de codigo

def saludar():
    print("Hola CILSA!")
    print("Buenas tardes!")
    print("Bienvenidos!")

# 2- llamada a una funcion
# para ejecutar un funcion, se escribe: su nombre seguido del parentesis

saludar()

# 3- funciones con parámetros
def saludar_persona(nombre):
    print(f"Hola {nombre}!")

saludar_persona("David")

# 4- funciones con valor de retorno
    # funcion que devuelve un resultado, usando return

def sumar(a, b):
    return a + b


a = int(input("Ingrese un numero: ")) # String --> Integer
b = int(input("Ingrese un numero: ")) # String --> Integer
resultado = sumar(a, b)
print(resultado)


print("Hola CILSA!")
print("Buenas tardes!")
print("Bienvenidos!")

print("Hola CILSA!")
print("Buenas tardes!")
print("Bienvenidos!")


print("Hola CILSA!")
print("Buenas tardes!")
print("Bienvenidos!")