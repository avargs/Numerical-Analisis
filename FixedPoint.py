import math

def truncate(num, dec):
    return math.floor(num * 10 ** dec) / 10 ** dec
def f(x):
	return x**2-x-1
def f2(x):
	return 1+(1/x)


def FixedPoint(li,ls):

	xi = (li+ls)/2
	xi = f2(xi)
	i = 1
	caja = xi+1

	while(truncate(xi,2) != truncate(caja,2)): 
		caja = xi
		xi = f2(xi)
		i=i+1

	print('Raiz aproximada:',xi)
	print('Valor anterior:',caja)
	print('Cantidad de iteraciones:',i)

FixedPoint(-4,3.75)
