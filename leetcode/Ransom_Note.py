#solution with count
def canConstruct(ransomNote: str, magazine: str):
    checker = set()
    for i in ransomNote:
        if i not in checker:
            checker.add(i)
            if ransomNote.count(i)>magazine.count(i):
                return False
    return True
print(canConstruct(ransomNote='a', magazine='b'))


