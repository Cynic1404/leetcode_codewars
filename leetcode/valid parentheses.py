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

# def isValid(s):
#     parentheses = {"{": "}", "(": ")", "[": "]"}
#     if len(s) < 2:
#         return False
#     a = list()
#     for el in s:
#         if el in parentheses:
#             a.append(el)
#         elif el not in parentheses:
#             if not len(a):
#                 return False
#             else:
#                 if parentheses[a[-1]] == el:
#                     a.pop()
#                 else:
#                     return False
#
#     return a == []


# def isValid(s):
#     dict = {"(": ")", "[": "]", "{": "}"}
#     check_list = []
#     for _ in s:
#         if len(check_list) == 0 and _ not in dict:
#             return False
#         elif len(check_list) > 0 and dict[check_list[-1]] == _:
#             check_list.pop()
#         elif len(check_list) > 0 and dict[check_list[-1]] != _ and _ not in dict:
#             return False
#         else:
#             check_list.append(_)
#     return check_list == []

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