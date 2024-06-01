import time as t
import random as r

el_tema = 'mi opinion sobre las elecciones'
art = ['mi ','tu ','su ']

i=0
while(i<10):
	print(el_tema + ' es una mierda')
	el_tema = art[r.randrange(3)] + 'opinion sobre ' + el_tema
	i = i+1
	t.sleep(1.9)


