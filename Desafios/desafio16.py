# Calcular el área de un triángulo
# Escribe una función llamada calcular_area_triangulo que reciba la base y la altura de un triángulo y devuelva su área.

# Prueba la función con diferentes valores de base y altura.
# Puedes incluir manejo de excepciones (opcional).

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dados la base y la altura."""
    try:
        base, altura = float(base), float(altura)
        return (base * altura) / 2 if base > 0 and altura > 0 else "Error: La base y la altura deben ser positivas."
    except ValueError:
        return "Error: Los valores ingresados deben ser numéricos."

# Pruebas con diferentes valores
pruebas = [(10, 5), (7, 3.5), ("a", 5), (-4, 6)]

for base, altura in pruebas:
    print(f"Base: {base}, Altura: {altura} → Área: {calcular_area_triangulo(base, altura)}")

