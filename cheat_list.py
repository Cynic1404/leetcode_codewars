### assignment
a = 5
b = 10
a, b = b, a
print(a, b)  # prints 10,5
###################################
a, b, c = 1, 2, 3  # a=1, b=2, c=3
##################################
tup = (1, 2, 3, 4, 5)
a, b, *other = tup
# a=1, b=2, other=[3,4,5]
*other, a, b, = tup
# other=[1,2,3], a=4, b=5




######### lambda

# lambda arguments : expression
x = lambda var: var + 10
print(x(5) == 15)
########################
print((lambda x, y: x+y)(1,2) == 3)
#########################

# Can be used like a standard function
b = (lambda x: 4+x)
print(b(6) == 10)







######### lists
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for i, m in enumerate(nums):
    print(i,m)
# 0 55
# 1 44
# 2 33
# 3 22
# 4 11




#### map/filter

def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
print(list(map(add_five, nums)) == [16, 27, 38, 49, 60])
# shorter version
print(list(map(lambda x: x + 5, nums)) == [16, 27, 38, 49, 60])
#####################################################

print(list(filter(lambda x: x > 33, nums)) == [44, 55])

#### strings

print(", ".join(["spam", "eggs", "ham"]) == "spam, eggs, ham")

print("Hello ME".replace("ME", "world") == "Hello world")

print("This is a sentence.".startswith("This") == True)

print("This is a sentence.".endswith("sentence.") == True)

print("This is a sentence.".upper() == "THIS IS A SENTENCE.")

print("AN ALL CAPS SENTENCE".lower() == "an all caps sentence")

print("spam, eggs, ham".split(", ") == ['spam', 'eggs', 'ham'])

#### print

print(*'kgf')
# prints "k g f"

print(*[1, 2, 3, 4, 5])
# prints "1 2 3 4 5"

print(*[1, 2, 3, 4, 5], sep='\n')


#### itreation
a = [[1, 2], [3, 4], [5, 6]]
for v, c in a:
    print(c, v)
#
# 1 2
# 3 4
# 5 6