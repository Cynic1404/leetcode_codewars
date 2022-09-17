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
print(pivotIndex([2,1,-1]))