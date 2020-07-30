def isAnagram(s, t):
    if len(s) == len(t) == 1 and s != t:
        return False
    if len(s) != len(t):
        return False
    if list(s).sort() == list(t).sort():
        return True

print(isAnagram('aa', 'bb'))