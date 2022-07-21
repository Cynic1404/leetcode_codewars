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


def isValid(s):
    dict = {"(": ")", "[": "]", "{": "}"}
    check_list = []

    for _ in s:
        if len(check_list)==0 and s[0] in dict.values():
            return False
        elif len(check_list) == 0:
            check_list.append(_)
        elif len(check_list) > 0:
            if _ == ")" and check_list[-1] == "(":
                check_list.pop(-1)
            elif _ == "]" and check_list[-1] == "[":
                check_list.pop(-1)
            elif _ == "}" and check_list[-1] == "{":
                check_list.pop(-1)
            else:
                check_list.append(_)
    return check_list==[]

print(isValid("()"))