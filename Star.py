def diamond(n):
	cspace = (n - 1) / 2
	cstar = 1
	
	if n % 2 != 0:
		while cstar < n:
			print " " * cspace + "*" * (cstar) + "\n"
			cspace -= 1
			cstar += 2
		
		print "*" * n + "\n"
		while cstar > 0:
			print " " * (cspace + 1) + "*" * (cstar - 2) + "\n"
			cspace += 1
			cstar -= 2
	else:
		return None
	
a = diamond(13)

