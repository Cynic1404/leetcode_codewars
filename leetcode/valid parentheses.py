def isValid(s):
    d = {")": '(', "]": "[", "}": "{"}
    stack = []
    for character in s:
        if character in d:
            if len(stack)>0 and stack[-1]==d[character]:
                stack.pop()
            else:
                return False
        else:
            stack.append(character)
    return stack==[]



#bad solution
# def isValid(s):
#     d = {"(": ')', "[": "]", "{": "}"}
#     s = list(s)
#     if len(s) % 2 != 0:
#         return False
#     if s[0] in d.values():
#         return False
#     counter = 0
#     while len(s) >= 2:
#         if s[counter] in d.values():
#             return False
#         if s[counter] in d:
#             if s[counter + 1] == d[s[counter]]:
#                 del s[counter]
#                 del s[counter]
#                 counter = 0
#             else:
#                 if len(s)==2:
#                     return False
#                 counter += 1
#                 if counter==len(s)-2:
#                     return False
#             if len(s) % 2 != 0:
#                 return False
#     return True





print(isValid("[(){}]"))