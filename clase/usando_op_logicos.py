""" 
Operadores lógicos en estructuras de control condicionales
and, or, not. 

El primero significa "y" donde existen operandos en ambos lados.
El segundo significa "o" donde existen operandos en ambos lados.
El tercero significa "no", se antepone a una variable o condicion,
si se antepone al valor True, el resultado será False, y viceversa,
por ejemplo:

condicion_1= = True
if not condicion_1:
    print("No cumple con la condicion 1")


"""

# Variables booleanas y numéricas
es_mayor = False
tiene_carnet = True
edad = 30

# Estructura de control usando operadores lógicos
if es_mayor and tiene_carnet:
    print("Cumple con ambos requisitos: es mayor y tiene carnet.")
elif es_mayor and edad <= 30:
    print("Es mayor de edad y tiene 30 años o menos.")
elif edad < 20 and tiene_carnet:
    print("Es menor de 20 años y tiene carnet.")
elif not es_mayor or not tiene_carnet:
    print("Falta cumplir con algún requisito.")
else:
    print("No se cumplen las condiciones.")

# Pueden ir cambiando los valores de las variables y probando los resultados.