import matplotlib.pyplot as plt
import numpy as np

"""
Funiones seno y coseno.
"""
# Definir el rango de valores para x, que abarque 2 pi radianes
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Definir las funciones seno y coseno
y_seno = np.sin(x)
y_coseno = np.cos(x)

# Crear la figura y el eje para la gráfica
fig, ax = plt.subplots()

# Graficar la función seno
ax.plot(x, y_seno, label='Seno')

# Graficar la función coseno
ax.plot(x, y_coseno, label='Coseno')

# Establecer títulos y etiquetas
ax.set_title('Gráficas de las Funciones Seno y Coseno')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Añadir una comentario para distinguir cada función
ax.legend()

# Mostrar la gráfica
plt.show()
