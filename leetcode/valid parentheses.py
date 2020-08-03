def isValid(s):
    d = {")": '(', "]": "[", "}": "{"}
    parentheses = []
    if len(s)==1:
        return False
    for character in s:
        if character in d:
            if len(parentheses)==0:
                return False
            last_element = parentheses.pop()
            if d[character] != last_element:
                return False
            else:
                continue
        else:
            parentheses.append(character)
    if len(parentheses)!=0:
        return True

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





print(isValid("(("))