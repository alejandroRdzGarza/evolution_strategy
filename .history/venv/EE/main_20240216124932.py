


#checar que una solucion este dentro del espacio de busqueda

def in_bounds(point, bounds):
    for dim in range(len(bounds)):
        if point[d] < bounds[d,0] or point[d] > bound[d,1 ]