def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0 or haystack == needle:
        return 0
    if len(haystack) < len(needle):
        return -1
    for n in range(len(needle)):
        for h in range(len(haystack) - len(needle) + 1):
            if needle[n] == haystack[h]:
                for g in range(len(needle)):
                    if needle[n + g] != haystack[h + g]:
                        break
                    else:
                        if g == len(needle) - 1:
                            return h
        return -1






print(strStr("mississippi", "issip"))
# print(strStr(haystack = "hello", needle = "ll"))
# print(strStr(haystack = "aaaaa", needle = "bba"))
# print(strStr("aaa","aaaa"))


"mississippi"
"issipi"
