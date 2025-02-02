from collections import defaultdict


def checkInclusion(s1, s2):
    s1_checker = defaultdict(int)
    for i in s1:
        s1_checker[i] += 1

    left = 0
    temp_checker = defaultdict(int)
    for right in range(len(s2)):
        temp_checker[s2[right]] += 1
        while temp_checker[s2[right]] > s1_checker[s2[right]]:
            temp_checker[s2[left]] -= 1
            left += 1
        if temp_checker == s1_checker:
            return True

    return False

assert checkInclusion(s1 = "ab", s2 = "eidbaooo") == True
assert checkInclusion(s1 = "ab", s2 = "eidboaoo") == False