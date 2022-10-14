
# def lengthOfLastWord(s):
#     return len(s.split()[-1])

def lengthOfLastWord(s):
    l = 0
    for i in range(-1, -len(s)-1, -1):
        if s[i] != " ":
            l += 1
        elif s[i] == " " and l:
            return l
        elif s[i] == " " and not l:
            continue
    return l

print(lengthOfLastWord("Hello World"))
