def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0 or haystack == needle:
        return 0
    if len(haystack) < len(needle):
        return -1
    for h in range(len(haystack) - len(needle) + 1):
        print(haystack[h:h+len(needle)])
        if haystack[h:h+len(needle)] == needle:
            return h
    return -1


print(strStr("mississippi", "issi"))