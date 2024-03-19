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
    
    plt.figure(figsize=(10, 6))
    contour = plt.contour(X, Y, Z, levels=35, cmap='viridis')
    plt.colorbar(contour)
    plt.title("Evolutionary Strategy Optimization")
    plt.xlabel('X')
    plt.ylabel('Y')
    
    

    
    
    


    