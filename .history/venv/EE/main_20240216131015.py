import random
import numpy as np


#checar que una solucion este dentro del espacio de busqueda
def in_bounds(point, bounds):
    for dim in range(len(bounds)):
        if point[dim] < bounds[dim,0] or point[dim] > bounds[dim, 1]:
            return False
    return True


# Algoritmo (mu + lambda)-EE

def ee_mas(funcion_objetivo, limites, iter_n, step_size, mu, lam):
    mejor, mejor_eval = None, 1e+10
    
    tam_pob, tam_sel = lam, mu
    
    n_hijos = int(tam_pob / tam_sel)
    
    
    #poblacion inicial
    poblacion = list()
    
    for _ in range(tam_pob):
        candidato = None
        
        while candidato is None or not in_bounds(candidato, limites):
            candidato = limites[:, 0] + random.rand(len(limites)) * (limites[:, 1] - limites[:,0])
            poblacion.append(candidato)
            
    #realizar la busqueda
    for epoch in range(iter_n):
        #evaluar aptitud de la poblacion
        aptitudes = [funcion_objetivo(c) for c in poblacion]
        
        # rankear las aptitudes en orden ascendente
        ranking = np.argsort(np.argsort(aptitudes))
        
        #seleccionar indices de las mejores soluciones dentro de mu
        seleccionados = [i for i,_ in enumerate(ranking) if ranking[i] < mu]
        
        #crear hijos
        hijos = list()
        for i in seleccionados:
            #revisar si este padre es el mejor visto
            if aptitudes[i] < mejor_eval:
                mejor, mejor_eval = poblacion[i], aptitudes[i]
                print("%d, Best:")