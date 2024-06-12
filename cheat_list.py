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

a = [1,2,3]
b=[4,5]
a.extend(b) # [1,2,3,4,5]

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


############ unpacking

def three(a,b,c):
    return a*b+c

z = [2,3,4]
print(three(*z))
#10

def f(*args):
    print("Positional:", args)
f(100, 50, 25)
#Positional: (100, 50, 25)

def f(**kwargs):
    print("Named:", kwargs)
f(galleons=100, sickles=50, knuts=25)
#Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}

d = {"c":4, "a":5, "b":3}
print(three(**d))
#19


#########
#dict_comprehension
students = ["Bob", "John", "Carry"]
students_dict = {student: "Chemistry" for student in students}
print(students_dict)
#{'Bob': 'Chemistry', 'John': 'Chemistry', 'Carry': 'Chemistry'}



######## setters and getters
class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        return f"{self.name}"

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        if sex not in ['male', 'female']:
            raise ValueError
        self._sex = sex


misha = Human("Mishka", "h")

