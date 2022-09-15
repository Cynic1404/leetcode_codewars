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

print(isAnagram('anna', 'nnaa'))