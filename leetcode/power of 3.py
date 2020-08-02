def isPowerOfThree(n):
    if n % 3 == 0:
        return isPowerOfThree(n//3)
    elif n==1:
        return True
    else:
        return False


# def isPowerOfThree(n):
#     if n == 0:
#         return False
#     while n % 3 == 0:
#         n = n // 3
#     if n == 1:
#         return True
#     return False




print(isPowerOfThree(27))

