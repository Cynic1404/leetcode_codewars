def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return -1
    res = {}
    for i in s:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    l = []

    for key, value in res.items():
        if value == 1:
            l.append(key)
    if len(l)==0:
        return -1
    for i in range(len(s)):
        if s[i] in l:
            return i


print(firstUniqChar('leetcode'))

