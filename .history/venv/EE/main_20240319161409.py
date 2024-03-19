import ee
import numpy as np
import funciones

#Constantes
np.random.seed(1)

#definir rango para input
limites = np.asarray([[-5.0, 5.0], [-5.0, 5.0]])

#definir el numero total de iteraciones
iter_n = 10000

#definir el step size maximo
step_size = 0.15

#numero de padres seleccionados
mu = 10

#numero de hijos generados por padres
lam = 10

lista_funciones = ["Rosenbrock", "Rastrigin", "Ackley", "McCormick", "Sum_squares"]


for i in range(len(lista_funciones)):
    print(str(i+1)+". "+ lista_funciones[i])

opcion = int(input("Escribe el numero de la funcion a utilizar"))

funcion_objetivo_prueba = "ackley"

#realizr la busqueda (mu + lambda)-EE
mejor, aptitud, history = ee.ee_mas(funciones.funcion_objetivo, limites, iter_n, step_size, mu, lam, opcion)
print("Done!")
print("f(%s) = %f" % (mejor, aptitud))
print(lista_funciones[opcion] + " function's global minimum is at:")
r_min, r_max = 0, 0
if opcion == 1:
    print("F(x*) = 0, at x* = (1, 1)")
    r_min, r_max = -5, 10
elif opcion == 2:
    print("F(x*) = 0, at x* = (0, 0)")
    r_min, r_max = -5.12, 5.12
elif opcion == 3:
    print("F(x*) = 0, at x* = (0, 0)")
    r_min, r_max = -32.768, 32.768
elif opcion == 4:
    print("F(x*) = -1.9133, at x* = (-0.54719, -1.54719)")
    r_min, r_max = -1.5, 4
elif opcion == 5:
    print("F(x*) = 0, at x* = (0, 0)")
    r_min, r_max = -10, 10
    

funciones.function_plot(r_min, r_max, history, opcion)

