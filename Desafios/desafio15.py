# Contar vocales
# Escribe una función llamada contar_vocales que reciba una palabra y devuelva cuántas vocales contiene.

# La función debe ignorar si las letras son mayúsculas o minúsculas.
# Usen la siguiente variable que guarda todas las vocales: vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
# Al final, prueba la función con diferentes palabras.
# (Nota: Asumimos que el usuario ingresará una palabra).

def contar_vocales(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = sum(1 for letra in palabra if letra in vocales)
    return contador

# Pruebas con diferentes palabras
palabras_de_prueba = ["Python", "inteligencia", "Artificial", "Éxito"]
for palabra in palabras_de_prueba:
    print(f"La palabra '{palabra}' tiene {contar_vocales(palabra)} vocales.")
