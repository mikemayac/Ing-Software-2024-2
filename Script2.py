# Ejercicio 1: Valles
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


# Ejercicio 2: Arbol binario
class Nodo:
    """
    Clase para representar un nodo en un árbol binario ordenado.

    Atributos:
    - valor (Any): El valor almacenado en el nodo.
    - izquierdo (Nodo): Referencia al nodo hijo izquierdo.
    - derecho (Nodo): Referencia al nodo hijo derecho.
    """

    def __init__(self, valor):
        """
        Inicializa un nuevo nodo con el valor dado.

        Parámetros:
        - valor (Any): El valor que se almacenará en el nodo.
        """
        self.valor = valor
        self.izquierdo = None  # Inicialmente no tiene hijo izquierdo.
        self.derecho = None    # Inicialmente no tiene hijo derecho.


class ArbolBinarioOrdenado:
    """
    Clase para representar un árbol binario ordenado.

    Atributos:
    - raiz (Nodo): La raíz del árbol binario ordenado.
    """

    def __init__(self):
        """
        Inicializa un nuevo árbol binario ordenado vacío.
        """
        self.raiz = None

    def agregar(self, valor):
        """
        Agrega un nuevo valor al árbol binario ordenado.

        Parámetros:
        - valor (Any): El valor que se agregará al árbol.
        """
        if not self.raiz:
            self.raiz = Nodo(valor)  # Si el árbol está vacío, el nuevo valor se convierte en la raíz.
        else:
            self._agregar(valor, self.raiz)  # De lo contrario, se busca la posición correcta para el nuevo valor.

    def _agregar(self, valor, nodo):
        """
        Método auxiliar recursivo para agregar un nuevo valor al árbol en la posición correcta.

        Parámetros:
        - valor (Any): El valor que se agregará al árbol.
        - nodo (Nodo): El nodo actual en el árbol durante la recursión.
        """
        if valor <= nodo.valor:
            if nodo.izquierdo:
                self._agregar(valor, nodo.izquierdo)
            else:
                nodo.izquierdo = Nodo(valor)
        else:
            if nodo.derecho:
                self._agregar(valor, nodo.derecho)
            else:
                nodo.derecho = Nodo(valor)

    def recorrido_pre_orden(self, nodo=None):
        """
        Realiza un recorrido pre-orden del árbol e imprime los valores de los nodos.

        Parámetros:
        - nodo (Nodo, opcional): El nodo actual en el árbol durante la recursión. Si es None, se inicia con la raíz.
        """
        if nodo is None:
            nodo = self.raiz
        print(nodo.valor, end=' ')
        if nodo.izquierdo:
            self.recorrido_pre_orden(nodo.izquierdo)
        if nodo.derecho:
            self.recorrido_pre_orden(nodo.derecho)

    def recorrido_in_orden(self, nodo=None):
        """
        Realiza un recorrido in-orden del árbol e imprime los valores de los nodos.

        Parámetros:
        - nodo (Nodo, opcional): El nodo actual en el árbol durante la recursión. Si es None, se inicia con la raíz.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo.izquierdo:
            self.recorrido_in_orden(nodo.izquierdo)
        print(nodo.valor, end=' ')
        if nodo.derecho:
            self.recorrido_in_orden(nodo.derecho)

    def recorrido_post_orden(self, nodo=None):
        """
        Realiza un recorrido post-orden del árbol e imprime los valores de los nodos.

        Parámetros:
        - nodo (Nodo, opcional): El nodo actual en el árbol durante la recursión. Si es None, se inicia con la raíz.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo.izquierdo:
            self.recorrido_post_orden(nodo.izquierdo)
        if nodo.derecho:
            self.recorrido_post_orden(nodo.derecho)
        print(nodo.valor, end=' ')


# Casos de prueba para el arbol binario ordenado.

# Caso de prueba 1
arbol = ArbolBinarioOrdenado()
arbol.agregar(3)
arbol.agregar(1)
arbol.agregar(4)
print("Recorrido In-Orden para el Caso de Prueba 2:")
arbol.recorrido_in_orden()
print("\n")

# Caso de prueba 2
print("Recorrido Pre-Orden para el Caso de Prueba 3:")
arbol.recorrido_pre_orden()
print("\n")

# Caso de prueba 3
print("Recorrido Post-Orden para el Caso de Prueba 4:")
arbol.recorrido_post_orden()
print("\n")

# Caso de prueba 4
arbol = ArbolBinarioOrdenado()
for valor in [5, 3, 7, 2, 4, 6, 8]:
    arbol.agregar(valor)
print("Recorrido In-Orden para el Caso de Prueba 5:")
arbol.recorrido_in_orden()
print("\nRecorrido Pre-Orden:")
arbol.recorrido_pre_orden()
print("\nRecorrido Post-Orden:")
arbol.recorrido_post_orden()
