import math

def truncate(num, dec):
    return math.floor(num * 10 ** dec) / 10 ** dec
def f(x):
	return 3*math.cos(x)-2
def df(x):
	return -3*math.sin(x)


def NewtonRap(li,ls):

	xi = (li+ls)/2
	xi = xi - f(xi)/df(xi)
	i = 1
	caja = xi+1

	while(truncate(xi,2) != truncate(caja,2)): 
		caja = xi
		xi = xi - f(xi)/df(xi)
		i=i+1

	print('Raiz aproximada:',xi)
	print('Valor anterior:',caja)
	print('Cantidad de iteraciones:',i)

NewtonRap(-1,6)
