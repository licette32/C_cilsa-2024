# Verificación de DNI en el sistema.
# Descripción: Crea una lista predefinida de números de DNI, por ejemplo: [12345678, 87654321, 11111111, 22222222].
# El programa deberá permitir al usuario ingresar un número de DNI y verificar si está registrado en la lista.

#Funcionalidades requeridas:

# Si el DNI se encuentra en la lista:
# Mostrar el mensaje: "El DNI xxx se encuentra registrado en nuestro sistema."
# Si el DNI no se encuentra:
# Mostrar el mensaje: "El DNI xxx no está registrado en nuestro sistema."
# Si la entrada no es un número:
# Mostrar el mensaje: "Lo lamento, xxx no es un número."
# Si el programa se ejecuta sin errores:
# Mostrar el mensaje: "¡El programa se ejecutó perfectamente!"
# Mensajes adicionales:

# Siempre mostrar un mensaje final al salir del programa, como: "Gracias por utilizar nuestro sistema."

# Opcional:
# Permitir al usuario realizar múltiples búsquedas hasta que decida salir escribiendo "salir".

def verificar_dni():
    # Lista de DNIs registrados en el sistema
    dni_registrados = [12345678, 87654321, 11111111, 22222222]
    
    while True:
        # Se le solicita al usuario que ingrese un DNI o la palabra 'salir'
        entrada = input("Ingrese un número de DNI o escriba 'salir' para finalizar: ")
        
        # Verificamos si el usuario quiere salir del programa
        if entrada.lower() == "salir":
            break
        
        # Comprobamos si el valor de entrada es un número
        if not entrada.isdigit():
            print(f"Lo lamento, {entrada} no es un número.")
            continue
        
        # Convertir la entrada en un número entero
        dni = int(entrada)
        
        # Verificar si el DNI está en la lista de registrados
        if dni in dni_registrados:
            print(f"El DNI {dni} se encuentra registrado en nuestro sistema.")
        else:
            print(f"El DNI {dni} no está registrado en nuestro sistema.")
    
    # Mensaje de finalización del programa
    print("¡El programa se ejecutó perfectamente!")
    print("Gracias por utilizar nuestro sistema.")

# Ejecutar la función
verificar_dni()
 