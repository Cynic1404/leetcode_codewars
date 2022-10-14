def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    search_index = 0
    letter_found = 0
    for letter in s:
        while search_index < len(t):
            if t[search_index] == letter:
                search_index += 1
                letter_found += 1
                break
            else:
                search_index += 1
    return letter_found == len(s)

print(isSubsequence('acb', 'ahbgdc'))


