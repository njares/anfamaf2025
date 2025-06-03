from ej1 import intenumcomp

def cuadratura_adaptativa(fun, I, tol):
	a, b = I
	c = (a+b)/2
	q = intenumcomp(fun, a, b, 2, "simpson")
	q1 = intenumcomp(fun, a, c, 2, "simpson")
	q2 = intenumcomp(fun, c, b, 2, "simpson")
	if abs(q-q1-q2) < 15*tol:
		return q1+q2
	else:
		q1_nuevo = cuadratura_adaptativa(fun, [a,c], tol/2)
		q2_nuevo = cuadratura_adaptativa(fun, [c,b], tol/2)
		return q1_nuevo + q2_nuevo
