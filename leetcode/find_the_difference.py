def findTheDifference(s: str, t: str):
    checker = {}
    for i in s:
        if i in checker:
            checker[i]+=1
        else:
            checker[i]=1

    for i in t:
        if i in checker:
            checker[i]+=1
        else:
            checker[i]=1

    for letter in checker:
        if checker[letter]==1 or checker[letter] %2!= 0:
            return letter

#unefficitent
# def findTheDifference(s: str, t: str):
#     for i in s:
#         s =s.replace(i, "", 1)
#         t=t.replace(i, "", 1)
#     return min(s,t)



print(findTheDifference(s = "abcd", t = "abcde"))

# print(findTheDifference(s = "a", t = "aa"))