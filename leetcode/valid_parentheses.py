# def isValid(s):
#     s=list(s)
#     dict = {"(":")", "[":"]", "{":"}"}
#     if len(s)%2!=0:
#         return False
#     else:
#         for opa in range(len(s)):
#             if s[0] in dict.values():
#                 return False
#             for _ in range(1, len(s)):
#                     if s[_] == dict[s[0]]:
#                         s.pop(0)
#                         _-= 1
#                         s.pop(_)
#                         if len(s) == 0:
#                             return True
#                         elif len(s) == 1:
#                             return False
#                         break
#         return False


# print(isValid("[)"))

def isValid(s):
    s=list(s)
    dict = {"(":")", "[":"]", "{":"}"}
    if len(s) % 2 != 0:
        return False
    else:
        while len(s)>1:
            for _ in range(len(s)):
                if s[_] in dict.values():
                    return False
                if len(s) == 1 or len(s) == 2 and s[1] != dict[s[0]]:
                    return False
                if len(s) == 0 or len(s) == 2 and s[1] == dict[s[0]]:
                    return True
                if s[_+1] == dict[s[_]]:
                    s.pop(_)
                    s.pop(_)
        return False


print(isValid("()"))