def isPalindrome(s):
    s = list(filter(lambda x:x.isalpha(), s))
    if len(s) in (0,1):
        return True
    for i in range(len(s) // 2):
        if s[i].lower() != s[-1 - i].lower():
            return False
    return True

print(isPalindrome("0P"))