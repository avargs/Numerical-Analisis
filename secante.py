import math

def f(x):
	return 3*math.cos(x)-2


def secante(p1,p2,error_tolerado):

	p2 = p2-(f(p2)*(p2-p1))/(f(p2)-f(p1))
	i = 1
	while(abs(p1-p2)>=error_tolerado):
		caja1 = p1
		caja2 = p2
		p2 = p2-(f(p2)*(p2-p1))/(f(p2)-f(p1))
		#print(p2)
		p1 = caja2
		i=i+1

	print('Raiz aproximada:',p2)
	print('Intervalo: [',caja1,'][',caja2,']')
	print('Cantidad de iteraciones:',i)


secante(-1,6,0.01)

#
