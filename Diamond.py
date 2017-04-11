def diamond(n):
	cspace = (n - 1) / 2
	cstar = 1
	nl = ''
	if n % 2 != 0:
		while cstar < n:
			nl += str(" " * cspace + "*" * (cstar) + "\n")
			cspace -= 1
			cstar += 2
			
		nl +=str("*" * n + "\n")
		
		while cstar > 0:
			nl += str(" " * (cspace + 1) + "*" * (cstar - 2) + "\n")
			cspace += 1
			cstar -= 2
		print nl
		return nl
	else:
		return None
diamond(9)