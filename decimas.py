import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

if(truncate(1.23456789,2) == truncate(1.23459876,2)):
	print('son iguales')