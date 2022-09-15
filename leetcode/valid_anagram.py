# def isAnagram(s, t):
#     if len(s) == len(t) == 1 and s != t:
#         return False
#     if len(s) != len(t):
#         return False
#     if list(s).sort() == list(t).sort():
#         return True
#
# def isAnagram(s, t):
#     return sorted(list(s)) == sorted(list(t))

def isAnagram(s, t):
    count_s = {}
    count_t = {}
    if len(s) == len(t):
        for _ in set(s):
            count_s[_] = s.count(_)
            count_t[_] = t.count(_)
    else:
        return False
    for i in count_s:
        if count_t[i] != count_s[i]:
            return False
    return True

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

print(isAnagram('anna', 'nnaa'))