def sortArrayByParity(nums):
    start = 0
    end = 0
    while end < len(nums):
        if nums[start] % 2 != 0:
            if nums[end] % 2 == 0:
                nums[end], nums[start] = nums[start], nums[end]
                start += 1
            end += 1
        else:
            start += 1
            end += 1
    return nums

print(sortArrayByParity([4,2,3,3,1,2,4,7,8,9]))