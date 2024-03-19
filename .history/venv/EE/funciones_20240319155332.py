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
def function_plot(r_min, r_max, history, numero_funcion):
    
    x = np.linspace(r_min, r_max, 400)
    y = np.linspace(r_min, r_max, 400)
    X, Y = np.meshgrid(x, y)
    
    
    Z = funcion_objetivo((X, Y), numero_funcion)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title("3D Visualization of function optimization")
    
    x_history = [point[0] for point in history]
    y_history = [point[1] for point in history]
    plt.plot(x_history, y_history, 'ro-', markersize=3, label='Path to Optimum')
    plt.legend()
    
    plt.show()

    
    
    


    