import math

def f(x):
	return 3*math.cos(x)-2


def biseccion(li,ls,error_tolerado):
	if (f(li)*f(ls)) >= 0:
		print('La función no cruza el eje X en el intervalo [',li,'',ls,']',)
		return	

	pm = (ls+li)/2

	i = 0

	while(abs(ls-li)>=error_tolerado):
		if f(pm)*f(ls) > 0:
			ls=pm
		if f(pm)*f(li) > 0:
			li=pm
		if f(pm) == 0:
			print('La raiz exacta es:',pm)
			return
		pm = (ls+li)/2
		#print(pm)
		i=i+1

	print('Raiz aproximada:',pm)
	print('Intervalo: [',li,'][',ls,']')
	print('Cantidad de iteraciones:',i)


biseccion(-1,6,0.01)

#
