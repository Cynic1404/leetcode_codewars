def isPalindrome(s):
    s = "".join([x.lower() for x in filter(lambda x: x.isalnum(), s)])
    for i in range(len(s) // 2):
        if s[i].lower() != s[-i - 1].lower():
            return False
    return True

print(isPalindrome("ab2a"))