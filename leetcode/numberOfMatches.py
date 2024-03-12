def numberOfMatches(n):
    counter = 0
    while n > 1:
        if n%2 ==0:
            counter+=n//2
            n=n//2
        else:
            counter += n // 2
            n = n // 2 +1

print(numberOfMatches(14))