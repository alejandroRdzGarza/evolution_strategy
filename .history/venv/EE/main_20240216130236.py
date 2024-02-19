


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
        
        while candidato is None or not in_bounds()