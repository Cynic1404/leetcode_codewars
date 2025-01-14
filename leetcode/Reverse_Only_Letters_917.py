# def reverseOnlyLetters(s):
#     letters = [c for c in s if c.isalpha()]
#     ans = []
#     for i in s:
#         if i.isalpha():
#             ans.append(letters.pop())
#         else:
#             ans.append(i)
#
#     return "".join(ans)

def reverseOnlyLetters(s):
    left = 0
    right = len(s)-1
    s = list(s)
    while left<right:
        if s[left].isalpha() and s[right].isalpha():
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        elif not s[left].isalpha():
            left+=1
        elif not s[right].isalpha():
            right-=1

    return "".join(s)

assert reverseOnlyLetters("ab-cd") == "dc-ba"
assert reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"