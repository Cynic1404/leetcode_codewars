# def longestCommonPrefix(strs):
#     strs = sorted(strs, key=len)
#     pref = ""
#     for i in range(len(strs[0])):
#         for l in strs[1:]:
#             if strs[0][i] != l[i]:
#                 return "" if not pref else pref
#         pref += strs[0][i]
#     return "" if not pref else pref

def longestCommonPrefix(strs):
    strs = sorted(strs, key=len)
    pref = ""
    for i in range(len(strs[0])):
        for l in strs:
            if i==len(l) or strs[0][i] != l[i]:
                return pref
        pref+=strs[0][i]
    return pref


print(longestCommonPrefix(["a"]))