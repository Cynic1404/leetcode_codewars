
def maxVowels(s, k):
    res= 0
    for i in range(k):
        if s[i] in "aeiou":
            res += 1

    cur = res
    for i in range(k, len(s)):
        if s[i] in "aeiou":
            cur+=1
        if s[i-k] in "aeiou":
            cur-=1
        res = max(res, cur)

    return res