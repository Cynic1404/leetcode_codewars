#two dicts with cross checks
# better in terms of efficiency because it uses two dictionaries for O(1) lookup, leading to an O(n) time complexity.
def wordPattern(pattern, s):
    checker_pattern = {}
    checker_s = {}

    words = s.split()

    if len(words) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] in checker_pattern and checker_pattern[pattern[i]] != words[i]:
            return False
        if words[i] in checker_s and checker_s[words[i]] != pattern[i]:
            return False
        checker_pattern[pattern[i]] = words[i]
        checker_s[words[i]] = pattern[i]

    return True

# one dict
# def wordPattern(pattern, s):
#     checker = {}
#     s = s.split()
#     if len(s) != len(pattern):
#         return False
#
#     for i in range(len(pattern)):
#         if pattern[i] in checker:
#             if checker[pattern[i]] != s[i]:
#                 return False
#         else:
#             if s[i] in checker.values():
#                 return False
#
#         checker[pattern[i]] = s[i]
#
#     return True


assert wordPattern("abba","dog cat cat dog") == True
assert wordPattern("abba","dog cat cat fish") == False
assert wordPattern("aaaa","dog cat cat dog") == False
assert wordPattern("abba","dog dog dog dog") == False