#solution with count method
# def canConstruct(ransomNote: str, magazine: str):
#     checker = set()
#     for i in ransomNote:
#         if i not in checker:
#             checker.add(i)
#             if ransomNote.count(i)>magazine.count(i):
#                 return False
#     return True


def ransomw(ransomNote: str, magazine: str):
    checker_r = {}
    checker_m = {}
    for i in ransomNote:
        if i in checker_r:
            checker_r[i]=checker_r[i]+1
        else:
            checker_r[i]=1
    for i in magazine:
        if i in checker_m:
            checker_m[i]=checker_m[i]+1
        else:
            checker_m[i]=1
    for el in checker_r:
        if el not in checker_m or checker_r[el]>checker_m[el]:
            return False
    return True
print(canConstruct(ransomNote='123', magazine='12'))


