def division_segura(num1, num2):    
    try:
        resultado = num1 / num2
        return f"El resultado de la división es: {resultado}"
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Ambos argumentos deben ser números."

# Pruebas: probamos el comportamiento de mu funcion
print(division_segura(1,3)) # --> numero
print(division_segura(5,0)) # --> mensaje de error, div 0
print(division_segura("hola",3)) # --> mensaje de error de tipo
