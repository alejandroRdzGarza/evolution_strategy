


#checar que una solucion este dentro del espacio de busqueda
def in_bounds(point, bounds):
    for dim in range(len(bounds)):
        if point[dim] < bounds[dim,0] or point[dim] > bounds[dim, 1]:
            return False
    return True


# Algoritmo (mu + lambda)-EE

