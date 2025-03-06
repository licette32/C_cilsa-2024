# Tipos de datos
# Primitivos:
    # Cadena de texto: String (str)
    # Entero: Integer (int)
    # Flotante: Float (float) --> para numeros decimales
    # Booleano: Boolean (bool) --> guarda solo True o False
# Complejos básicos: Lista, Tuplas, Conjuntos, Diccionarios.

# "None" es un valor especial

# Nota: Existen otros tipos de datos complejos avanzados, y los que podemso crear nosotros en un futuro.


# LISTAS
# Secuencia ordenada de elementos y mutable
# Podemos acceder a sus elementos mediante un índice 
# Podemos tener elementos duplicados
# Podemos utilizar métodos
mi_lista = [1, 2, 3, 4]

# TUPLAS
# Son secuencias ordenadas e inmutables de elementos.
# Se definen utilizando paréntesis ( ).
# No se pueden modificar después de su creación.
# Permiten elementos duplicados.
# Se pueden acceder a los elementos mediante su índice.
# Son útiles para representar datos que no deben cambiar, como coordenadas geográficas.
mi_tupla = (1, 2, 3, 4)

# CONJUNTOS
# Colecciones desordenadas de elementos únicos.
# Se definen utilizando llaves { } junto con los elementos, o con la función set().
# No admiten elementos duplicados.
# No permiten acceso mediante índices, ya que no tienen un orden definido.
# Se pueden realizar operaciones de conjunto como unión, intersección y diferencia.
mi_conjunto = {1, 2, 3, 4}

# DICCIONARIOS
# Colecciones de pares clave-valor.
# Se definen utilizando llaves { }.
# Las claves son únicas e inmutables, mientras que los valores pueden ser de cualquier tipo y mutables.
# Se accede a los valores mediante sus claves, no mediante índices.
# Muy útiles para representar datos estructurados y para buscar eficientemente valores asociados con una clave.
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': [1,2,3]}


