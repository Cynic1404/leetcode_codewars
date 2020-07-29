def isPalindrome(x: int) -> bool:
    o = str(x)
    for i in range(len(o) // 2):
        print(o[i], o[len(o) - 1 - i] )
        if o[i] != o[len(o) - 1 - i]:
            return False
    return True

