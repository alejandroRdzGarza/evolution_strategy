

#Constantes
seed(1)

#definir rango para input
limites = asarray([[-5.0, 5.0], [-5.0, 5.0]])

#definir el numero total de iteraciones
iter_n = 5000

#definir el step size maximo
step_size = 0.15

#numero de padres seleccionados
mu = 10

#numero de hijos generados por padres
lam = 10

#realizr la busqueda (mu + lambda)-EE
mejor, aptitud = ee_mas(funcion_objetivo, limites, iter_n, step_size, mu, lam)
print("Done!")
print("f(%s) = %f")

