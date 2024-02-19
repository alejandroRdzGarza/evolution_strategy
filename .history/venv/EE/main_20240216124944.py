


#checar que una solucion este dentro del espacio de busqueda

def in_bounds(point, bounds):
    for dim in range(len(bounds)):
        if point[dim] < bounds[d,0] or point[d] > bounds[d, 1]