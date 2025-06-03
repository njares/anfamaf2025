import numpy as np

def soltrsup(A,b):
	"""
	Resuelve el sistema lineal Ax = b, donde A es una matriz triangular 
	superior.
	"""
	n = b.shape[0]
	x = np.empty((n,))
	for i in range(n-1,-1,-1):
		x[i] = b[i] - np.dot(A[i,i+1:],x[i+1:])
		# ~ for j in range(i+1,n):
			# ~ x[i] -= A[i,j]*x[j]
		if A[i,i] != 0:
			x[i] /= A[i,i]
		else:
			print("Error: Matriz singular")
			return None
	return x

def soltrinf(A,b):
	"""
	Resuelve el sistema lineal Ax = b, donde A es una matriz triangular 
	inferior.
	"""
	n = b.shape[0]
	x = np.zeros((n,))
	for i in range(n):
		x[i] = b[i] - np.dot(A[i,:i],x[:i])
		if A[i,i] != 0:
			x[i] /= A[i,i]
		else:
			print("Error: Matriz singular")
			return None
	return x
