def to_power(a,n):
    if n == 0:
        return 1
    elif n%2 ==1: #odd
        return to_power(a,n-1)*a
    else:
        return to_power(a**2, n//2) #even



print(to_power(5, 18))