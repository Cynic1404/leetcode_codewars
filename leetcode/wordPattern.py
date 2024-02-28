def wordPattern(pattern, s):
    checker = {}
    s = s.split()
    if len(s) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] in checker:
            if checker[pattern[i]] != s[i]:
                return False
        else:
            if s[i] in checker.values():
                return False

        checker[pattern[i]] = s[i]

    return True