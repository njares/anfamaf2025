def intenumcomp(fun,a,b,N,regla):
	if not (isinstance(N,int) and N>0):
		print("Error: N debe ser un entero positivo")
	if regla == 'trapecio':
		sx0 = fun(a) + fun(b)
		sx1 = 0
		h = ( b - a ) / N
		x = a
		for j in range(1,N):
			x = x + h
			sx1 = sx1 + fun(x)
		sx = (sx0 + 2 * sx1) * h / 2
		return sx
	elif regla == 'pm':
		if N % 2 == 1:
			N = N+1
		h = ( b - a ) / N
		x = a - h
		sx1 = 0
		for j in range(0,N//2):
			x = x + 2*h
			sx1 = sx1 + fun(x)
		sx = sx1 * 2*h
		return sx
	elif regla == 'simpson':
		if N % 2 == 1:
			N = N+1
		sx0 = fun(a) + fun(b)
		sx1 = 0
		sx2 = 0
		h = ( b - a ) / N
		x = a
		for j in range(1,N):
			x = x + h
			if j % 2 == 0:
				sx2 = sx2 + fun(x)
			else:
				sx1 = sx1 + fun(x)
		sx = (sx0 + 2 * sx2 + 4 * sx1) * h / 3
		return sx
	else:
		print("Regla inválida")
		return None
