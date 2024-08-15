def groupAnagrams(strs):
    res = {}
    for string in strs:
        key = ''.join(sorted(string))
        if key not in res:
            res[key] = [string]
        else:
            res[key].append(string)
    return list(res.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))