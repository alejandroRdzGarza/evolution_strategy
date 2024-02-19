# Funciones a optimizar

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcion_objetivo(x,y, nombre):
    if nombre.lower() == "ackley":
         
    elif nombre.lower() == "":


# metodo para visualizar una funcion, r_min y r_max representan el rango minimo y maximo
def function_plot(r_min, r_max, nombre_funcion):
    
    xaxis = np.arange(r_min, r_max, 0.1)
    yaxis = np.arange(r_min, r_max, 0.1)
    
    x, y = np.meshgrid(xaxis,yaxis)
    
    resultados = funcion_objetivo(x,y, nombre_funcion)
    