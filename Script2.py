def contar_valles(caminata: str) -> int:
    """
    Calcula el número de valles en una caminata.

    Un valle se define como una secuencia de pasos que comienza con un descenso bajo el nivel del mar ('D')
    y termina cuando se vuelve a subir al nivel del mar ('U'). La caminata siempre comienza y termina en el nivel del mar.

    Parámetros:
    - caminata (str): Una cadena de caracteres donde 'U' representa un paso hacia arriba y 'D' representa un paso hacia abajo.

    Retorna:
    - int: El número de valles recorridos durante la caminata.

    Ejemplo:
    >>> contar_valles("DDUU")
    1
    """

    nivel = 0  # Nivel del mar. Comienza en 0, indicando el nivel del mar al inicio de la caminata.
    valles = 0  # Contador de valles. Incrementa cada vez que se completa un valle.
    en_valle = False  # Indicador de si el caminante está actualmente en un valle.

    for paso in caminata:
        if paso == 'U':  # Si el paso es hacia arriba ('U'),
            nivel += 1  # incrementamos el nivel.
            if nivel == 0 and en_valle:  # Si regresamos al nivel del mar y estábamos en un valle,
                valles += 1  # contamos un valle y
                en_valle = False  # indicamos que ya no estamos en un valle.
        else:  # Si el paso es hacia abajo ('D'),
            if nivel == 0:  # y si estamos al nivel del mar,
                en_valle = True  # entramos a un valle.
            nivel -= 1  # Decrementamos el nivel.

    return valles  # Retornamos el número total de valles recorridos.


# Caso de prueba 1
entrada = "DDUU"
resultado_esperado = 1
resultado_obtenido = contar_valles(entrada)

print(f"Caso de prueba 1: {'Correcto' if resultado_obtenido == resultado_esperado else 'Incorrecto'}")
print(f"Entrada: {entrada}")
print(f"Resultado esperado: {resultado_esperado}")
print(f"Resultado obtenido: {resultado_obtenido}\n")

# Caso de prueba 2
entrada_larga = "DU" * 500  # Genera una cadena con 500 repeticiones de 'DU'
resultado_esperado_largo = 500
resultado_obtenido_largo = contar_valles(entrada_larga)

print(f"Caso de prueba largo: {'Correcto' if resultado_obtenido_largo == resultado_esperado_largo else 'Incorrecto'}")
print(f"Longitud de entrada: {len(entrada_larga)}")
print(f"Resultado esperado: {resultado_esperado_largo}")
print(f"Resultado obtenido: {resultado_obtenido_largo}\n")

