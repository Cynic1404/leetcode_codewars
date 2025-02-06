class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if i.isupper():
                    if stack[-1]==i.lower():
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    if stack[-1]==i.upper():
                        stack.pop()
                    else:
                        stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)



check = Solution()
assert check.makeGood("leEeetcode")=="leetcode"
assert check.makeGood("abBAcC")==""
assert check.makeGood("s")=="s"

