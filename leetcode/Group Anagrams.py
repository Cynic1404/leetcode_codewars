def groupAnagrams(strs):
    d = {}
    res = []
    for i in range(len(strs)):
        a = ''.join(sorted(list(strs[i])))
        if a not in d:
            d[a]=[strs[i]]
        else:
            d[a]=d[a]+[strs[i]]
    for i in d:
        res.append(d[i])
    return res

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))