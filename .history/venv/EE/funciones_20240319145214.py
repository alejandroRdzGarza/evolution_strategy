# Funciones a optimizar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. rosenbrock
# 2. rastrigin
# 3. ackley
# 4. mccormick
# 5. sum_squares

# TODO: Agregar las ecuaciones de las funciones que faltan
def funcion_objetivo(i, numero_funcion):
    x, y = i
    if numero_funcion == 3:
        return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20


# metodo para visualizar una funcion, r_min y r_max representan el rango minimo y maximo
def function_plot(r_min, r_max, nombre_funcion):
    
    x = np.linspace(r_min, r_max, 400)
    y = np.linspace(r_min, r_max, 400)
    
    X, Y = np.meshgrid(x, y)
    
    i = (x, y)
    resultados = funcion_objetivo(i, nombre_funcion)
    
    figure = plt.figure()
    ax = Axes3D(figure)
    ax.plot_surface(x, y, resultados, cmap='jet')
    plt.show()
    
    
    


    