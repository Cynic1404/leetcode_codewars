class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i not in ["", "..", "."]:
                stack.append(i)
            elif i == "..":
                if stack:
                    stack.pop()

        return "/"+"/".join(stack)


check = Solution()
assert check.simplifyPath("/home/")=="/home"
assert check.simplifyPath("/home//foo/")=="/home/foo"
assert check.simplifyPath("/home/user/Documents/../Pictures")=="/home/user/Pictures"
assert check.simplifyPath("/../")=="/"
assert check.simplifyPath("/.../a/../b/c/../d/./")=="/.../b/d"
assert check.simplifyPath("/a/../../b/../c//.//")=="/c"