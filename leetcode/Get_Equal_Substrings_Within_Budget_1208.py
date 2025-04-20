
#easier to understand
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    checker = []
    left = curr_cost = res = 0

    #create a list of differences between the ASCII values of the characters
    for i in range(len(s)):
        checker.append(abs(ord(t[i]) - ord(s[i])))

    for right in range(len(s)):
        curr_cost += checker[right]
        while curr_cost > maxCost:
            curr_cost -= checker[left]
            left += 1
        res = max(res, right - left + 1)
        right += 1

    return res

# refactored, less memory
# def equalSubstring(s: str, t: str, maxCost: int) -> int:
#     left = curr_cost = res = 0
#
#     for right in range(len(s)):
#         curr_cost += abs(ord(t[right]) - ord(s[right]))
#         while curr_cost > maxCost:
#             curr_cost -= abs(ord(t[left]) - ord(s[left]))
#             left += 1
#         res = max(res, right - left + 1)
#         right += 1
#
#     return res


assert equalSubstring( s = "abcd", t = "cdef", maxCost = 3) == 1
assert equalSubstring( s = "abcd", t = "cdef", maxCost = 3) == 1
assert equalSubstring( s = "abcd", t = "acde", maxCost = 0) == 1
assert equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19) == 2