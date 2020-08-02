def missingNumber(nums):
    nums = sorted(nums)
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return i+1

print(missingNumber([0]))