# 1 kg -> 10 m2

# P[g] >= 3 g
# N[g] >= 1.5 g
# K[g] >= 4 g

#	 T1 	T2
# P	3		2
# N	1		3
# K	8		2
# $ 10		8

# x : cantidad de Kg de fertilizante T1
# y : cantidad de Kg de fertilizante T2

# f.o. : 10 x + 8 y

# cantidad de g de P: 3x+2y
# cantidad de g de N: x+3y
# cantidad de g de K: 8x+2y

# el problema es:
# minimizar 10 x + 8 y
# s.a.		3x+2y >= 3
#			x+3y >= 1.5
#			8x+2y >= 4
#			x, y >= 0

from scipy.optimize import linprog
import numpy as np

c = np.array([10., 8.])
A_ub = np.array([[-3., -2. ],[-1., -3. ],[-8., -2.]])
b_ub = np.array([-3, -1.5, -4])

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0,None))

x_final = res.x
fun_final = res.fun
status = res.status
nit = res.nit

print(f"el algoritmo terminó con {status = } en {nit = }")
print(f"{x_final = }")
print(f"{fun_final = }")
