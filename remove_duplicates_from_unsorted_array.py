a = [1,1,1,12,2,2,2,4,5,6,7,8,9,7,7,6,5,4,3,2,1,1,1,1,11,1]
stack = set()
counter = 0
while len(a)>len(stack):
    if a[counter] in stack:
        a.pop(counter)
    else:
        stack.add(a[counter])
        counter+=1
print(a)