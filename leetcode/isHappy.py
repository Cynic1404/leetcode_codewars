def isHappy(n):
    sum = n
    res = 0
    stack = set()
    while True:
        for i in str(sum):
            res += int(i) ** 2
        sum = res
        if sum == 1:
            return True
        if sum in stack:
            return False
        else:
            stack.add(sum)
        res=0

print(isHappy('19'))
