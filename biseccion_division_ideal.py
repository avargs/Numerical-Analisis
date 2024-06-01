def division_biseccion(dividendo,divisor,li,ls,error_tolerado):
	pm=0
	error_calculado=dividendo
	while(abs(error_calculado)>error_tolerado):
		pm=(ls+li)/2
		error_calculado=dividendo-pm*divisor
		if(error_calculado>0):
			li=pm
		if(error_calculado<0):
			ls=pm
		if(error_calculado==0):
			print('El resultado es:',pm)
			print('El error es:',error_calculado)
	print('El resultado es:',pm)
	print('El error es:±',(abs(error_calculado)/2))


division_biseccion(60,3,4,100,0.0001)

#empezar desde ejemplo del mago yo soy el mago, tolero un error de tres num 2.5
#no valores aleatorios, hay un metodo
#division partes de primaria y mismo ejemplo
#tabla con pm, error, li,ls
#comenzar a construir pseudocodigo breaking down the steps
#dar un rango cuyo punto medio es el valor exacto thatll fuck em up
#dar un resultado fuera del rango
#repaso evaluacion de funciones
#programacion evaluacion de funciones
#ejemplo de biseccion pero con funcion sin codigo
#Y TAREA PARA EL FIN DE SEMANA