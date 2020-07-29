from math import sqrt

def is_square(n):
	if n < 0:
		return False
	elif int(sqrt(n)) == sqrt(n):
				
		return True
	else:
		return False
	
	