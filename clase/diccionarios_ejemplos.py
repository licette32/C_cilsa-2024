# Este archivo contiene ejemplos prácticos y ejercicios con diccionarios.

# Crear un diccionario para almacenar información de personas
lista_nombres = [
    ["David", "Perez", 22],
    ["Luis", "Gonzalez"],
    ["Esteban", "Diaz"]
]

diccionario = {
    'Persona1': {'Nombre': 'David', 'Apellido': 'Perez'},
    'Persona2': {'Nombre': 'Luis', 'Apellido': 'Gonzalez', 'Edad': 29}
}
print(diccionario)

# Crear un diccionario con información de 5 personas
# Nota: Este ejemplo repite datos para simplificar.
personas = {}  # También se puede usar `personas = dict()`
for i in range(5):
    clave = f'Persona{i + 1}'
    valor = {'Nombre': 'Juan'}
    personas[clave] = valor

print(personas)
