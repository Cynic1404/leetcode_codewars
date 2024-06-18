def isSubsequence(s: str, t: str) -> bool:
    x, y = 0, 0
    # Traverse through both strings
    while x < len(s) and y < len(t):
        if s[x] == t[y]:
            x += 1  # Move to the next character in s
        y += 1  # Move to the next character in t

    # If we've matched all characters in s, x will be equal to len(s)
    return x == len(s)

print(isSubsequence('acb', 'vahbgdcb'))


