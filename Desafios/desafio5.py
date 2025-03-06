
# Ingresar primero el limite inferior del intervalo y luego el limite posterior.

lim_inf = int(input("Ingrese el límite inferior del intervalo: "))
lim_sup = int(input("Ingrese el límite superior del intervalo: "))

# Ingresar el valor entero (Z)
valor_Z = int(input("Ingrese un valor entero: "))

# Verificar si el valor está dentro del intervalo
if lim_inf <= valor_Z <= lim_sup:
    print(f"El valor {valor_Z} está dentro del intervalo ({lim_inf}, {lim_sup}).")
else:
    print(f"El valor {valor_Z} NO está dentro del intervalo ({lim_inf}, {lim_sup}).")
