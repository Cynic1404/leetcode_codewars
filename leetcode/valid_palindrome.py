# def isPalindrome(s):
#     s = "".join([x.lower() for x in filter(lambda x: x.isalnum(), s)])
#     for i in range(len(s) // 2):
#         if s[i].lower() != s[-i - 1].lower():
#             return False
#     return True

#faster , two pointers

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("ab2a"))