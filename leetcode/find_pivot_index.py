def pivotIndex(nums):
    right = sum(nums[1:])
    left = 0
    if right != 0:
        for i in range(1, len(nums)):
            left +=nums[i-1]
            right -= nums[i]
            if left==right:
                return i
    else:
        return 0
    return -1

#faster solution, not mine
def pivotIndex(nums):
    sumL = 0
    sumR = sum(nums)
    for i in range(len(nums)):
        sumR -= nums[i]
        if sumL == sumR:
            return i
        sumL += nums[i]
    return -1

print(pivotIndex([1,7,3,6,5,6]))