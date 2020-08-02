# def longestCommonPrefix(strs):
#     if len(strs) == 0 or len(strs[0]) == 0:
#         return ""
#     first_word = strs[0]
#     for index_of_letter in range(len(first_word)):
#         for word in range(len(strs[:-1])):
#             if strs[word + 1] == "":
#                 return ""
#             elif len(strs[word + 1]) == index_of_letter:
#                 return strs[word + 1]
#             else:
#                 if strs[word][index_of_letter] == strs[word + 1][index_of_letter]:
#                     continue
#                 return first_word[:index_of_letter]
#     return first_word

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    res = ''
    strs = sorted(strs)
    for i in strs[0]:
        if strs[-1].startswith(res + i):
            res += i
        else:
            break
    return res

print(longestCommonPrefix(["aaac","aaaaaaaaaaaab","aaaaaaa"]))