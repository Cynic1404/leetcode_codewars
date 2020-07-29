"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]"""


def unique_in_order(iterable):
	result = []
	first = -1
	second = 0
	if iterable == []:
		return []
	elif len(iterable) == 1 or len(iterable) == 2 and iterable[0]==iterable[1]:
		result.append(iterable[0])
	for i in iterable:
		if iterable[first]!=iterable[second]:
			result.append(i)
			print result
			first+=1
			second+=1
		else:
			print first
			print second
			first +=1
			second += 1
	return result


			
			