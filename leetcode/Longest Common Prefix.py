def longestCommonPrefix(strs):
    longest_prefix = ""
    for i in range(len(strs[0])):
        letter_to_compare = strs[0][i]
        for word in strs[1:]:
            if i == len(word) or word[i] != letter_to_compare:
                return longest_prefix
        longest_prefix += strs[0][i]
    return longest_prefix

print(longestCommonPrefix(["flower","flow","flight"]))
# def longestCommonPrefix(strs):
#     if len(strs) == 0:
#         return ''
#     res = ''
#     strs = sorted(strs)
#     for i in strs[0]:
#         if strs[-1].startswith(res + i):
#             res += i
#         else:
#             break
#     return res

print(longestCommonPrefix(["aaac","aaazaaaaaaab","aaaaaaa"]))