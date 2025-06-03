from scipy.linal import lu
from ej3 import soltrinf, soltrsup

def sollu(A,b):
	P, L, U = lu(A)
	P_inv = P.T
	y = soltrinf(L, P_inv@b)
	x = soltrsup(U, y)
	return x

