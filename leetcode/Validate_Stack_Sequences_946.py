class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack=[]
        pop_pointer=0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[pop_pointer]:
                stack.pop()
                pop_pointer+=1

        return len(stack) == 0

check = Solution()
assert check.validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
assert check.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) == False
assert check.validateStackSequences([1,0], [1,0])