"""

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
"""

def tower_builder(n_floors):
	result = []
	
	strings = n_floors
	f_stars = 1 + 2 * (n_floors - 1)
	stars = 1
	prob = (f_stars - stars) / 2
	
	for i in range(strings):
		result.append(" " * prob + "*" * stars + " " * prob)
		stars += 2
		prob -= 1
	
	print result


	for i in result:
		print i + "\n"
	return result