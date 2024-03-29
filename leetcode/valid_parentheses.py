# def isValid_bruteforce(s):
#     s = list(s)
#     dict = {"(": ")", "[": "]", "{": "}"}
#     if len(s) % 2 != 0:
#         return False
#     else:
#         while len(s) > 1:
#             for _ in range(len(s)):
#                 if s[_] in dict.values():
#                     return False
#                 if len(s) == 1 or len(s) == 2 and s[1] != dict[s[0]]:
#                     return False
#                 if len(s) == 0 or len(s) == 2 and s[1] == dict[s[0]]:
#                     return True
#                 if s[_ + 1] == dict[s[_]]:
#                     s.pop(_)
#                     s.pop(_)
#                     break
#         return False


# def isValid(s):
#     dict = {"(": ")", "[": "]", "{": "}"}
#     check_list = []
#     for _ in s:
#         if len(check_list) == 0 and _ in dict.keys():
#             check_list.append(_)
#         elif len(check_list) == 0 and _ in dict.values():
#             return False
#         elif len(check_list) > 0:
#             if dict[check_list[-1]] == _:
#                 check_list.pop(-1)
#             elif dict[check_list[-1]] != _ and _ in dict.values():
#                 return False
#             else:
#                 check_list.append(_)
#     return check_list == []

# def isValid(s):
#     dict = {"(": ")", "[": "]", "{": "}"}
#     check_list = []
#     for _ in s:
#         if len(check_list) == 0 and _ not in dict.keys():
#             return False
#         elif len(check_list) > 0 and dict[check_list[-1]] == _:
#             check_list.pop(-1)
#         elif len(check_list) > 0 and dict[check_list[-1]] != _ and _ not in dict.keys():
#             return False
#         else:
#             check_list.append(_)
#     return check_list == []


def isValid(s):
    dict = {")": "(", "]": "[", "}": "{"}
    check_list = []
    for _ in s:
        if _ in dict:
            if len(check_list) > 0 and check_list[-1] == dict[_]:
                check_list.pop()
            else:
                return False
        else:
            check_list.append(_)
    return check_list == []



print(isValid("){"))
print(isValid("([)]"))
print(isValid("()"))
print(isValid("(]"))
print(isValid("()[]{}"))
