# Funciones a optimizar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. rosenbrock
# 2. rastrigin
# 3. ackley
# 4. mccormick
# 5. sum_squares

def funcion_objetivo(i, numero_funcion):
    x, y = i
    if numero_funcion == 1:
        return ((x - 1) ** 2) + (100 * (y - x**2) ** 2)
    
    elif numero_funcion == 2:
        return 30 + (x**2 - 10* np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y))
        
    elif numero_funcion == 3:
        return -0.2 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20
    
    elif numero_funcion == 4:
        return np.sin(x + y) + (x - y)**2 - 1.5 * x + 2.5 * y + 1
        
    elif numero_funcion == 5:
        return (1 * x**2) + (2 * y**2)


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
    z_history = [funcion_objetivo(point, numero_funcion) for point in history]
    
    ax.plot(x_history, y_history, z_history, 'r.-', markersize=5, label='Optimization Path')
    ax.legend()
    
    plt.show()
    
    


    