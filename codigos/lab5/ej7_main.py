from ej7 import cuadratura_adaptativa
import numpy as np

def fun(x):
	return x*np.exp(-x*x)

integral_aprox = cuadratura_adaptativa(fun, [0,1], 1e-5)
integral_exacta = (1/2)*(1-np.exp(-1))

print(f"{integral_aprox = }")
print(f"{integral_exacta = }")
