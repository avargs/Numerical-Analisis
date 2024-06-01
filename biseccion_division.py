def division_biseccion(dividendo,divisor,li,ls,error_tolerado):
	pm=0
	while(abs(dividendo-pm*divisor)>error_tolerado):
		pm=(ls+li)/2
		if(dividendo<pm*divisor):
			ls=pm
		if(dividendo>pm*divisor):
			li=pm
		if(dividendo==pm*divisor):
			print('La respuesta exacta:',pm)
		print('El intervalo es [',li,'',ls,']')
	print('La respuesta aproximada es:',pm)
	print('El error es: +-',dividendo/divisor-pm)


division_biseccion(80,4,11,30,0.1)
