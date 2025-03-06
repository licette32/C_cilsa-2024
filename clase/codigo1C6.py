# DICCIONARIO: SE COMPONE DE CLAVE-VALOR (KEY-VALUE EN INGLÉS)
mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Mar del Plata'
}

# Acceder a valores en un diccionario
nombre = mi_diccionario['nombre']  # Usando corchetes
edad = mi_diccionario.get('edad', "Clave no encontrada")  # Usando el método get
print(f"Nombre: {nombre}, Edad: {edad}")

# Modificar valores en un diccionario
mi_diccionario['ciudad'] = "La Plata"  # Modificando directamente
mi_diccionario.update({'ciudad': 'Lanus'})  # Usando el método update para modificar sobre una clave existente
mi_diccionario.update({'curso': 'Python'})  # También podemos usarlo para agregar una clave-valor
print("Diccionario actualizado:", mi_diccionario)

# Agregar un nuevo par clave-valor
mi_diccionario['profesion'] = "Programador"
print("Con nueva clave 'profesion':", mi_diccionario)
# Nota: podemos usar el update.

# Eliminar elementos del diccionario
del mi_diccionario['edad']  # Usando del
print("Sin la clave 'edad':", mi_diccionario)
ciudad_eliminada = mi_diccionario.pop('ciudad', 'Clave no encontrada')  # Usando pop
print(f"La ciudad eliminada fue: {ciudad_eliminada}")
print("Estado final del diccionario:", mi_diccionario)
