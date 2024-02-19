# Funciones a optimizar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcion_objetivo(x,y, nombre):
    if nombre.lower() == "ackley":
        return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20


# metodo para visualizar una funcion, r_min y r_max representan el rango minimo y maximo
def function_plot(r_min, r_max, nombre_funcion):
    
    xaxis = np.arange(r_min, r_max, 0.1)
    yaxis = np.arange(r_min, r_max, 0.1)
    
    x, y = np.meshgrid(xaxis,yaxis)
    
    resultados = funcion_objetivo(x, y, nombre_funcion)
    
    figure = plt.figure()
    ax = Axes3D(figure)
    ax.plot_surface(x, y, resultados, cmap='jet')
    plt.show()
    
    
function_plot(-5.0, 5.0, "ackley")
    