import ee
import numpy as np
import funciones

#Constantes
np.random.seed(1)

#definir rango para input
limites = np.asarray([[-5.0, 5.0], [-5.0, 5.0]])

#definir el numero total de iteraciones
iter_n = 5000

#definir el step size maximo
step_size = 0.15

#numero de padres seleccionados
mu = 10

#numero de hijos generados por padres
lam = 10

lista_funciones = ["rosenbrock", "rastringin", "ackley", "mccormick", "sum_squares"]


for i in range(len(lista_funciones)):
    print(str(i+1)+". "+ lista_funciones[i])

opcion = int(input("Escribe el numero de la funcion a utilizar"))

funcion_objetivo_prueba = "ackley"

#realizr la busqueda (mu + lambda)-EE
mejor, aptitud = ee.ee_mas(funciones.funcion_objetivo, limites, iter_n, step_size, mu, lam, opcion)
print("Done!")
print("f(%s) = %f" % (mejor, aptitud))

