# SABER SI UN NUMERO ES PAR. Informar.
# UTILIZAR UNA FUNCION

## definimos una funcion

def es_par(n):
    if numero % 2 == 0:
        return True
    else:
        return False

# Vamos a preguntarnos si el numero es par: operador modulo %

# si numero % 2 == 0 es verdad --> es par
# sino es impar.
numero = 6
booleano_es_par = es_par(numero)

if booleano_es_par:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} no es un número par.")

