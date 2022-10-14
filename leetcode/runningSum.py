def runningSum(nums):
    for i in range(len(nums) - 1):
        nums[i + 1] = nums[i] + nums[i + 1]
    return (nums)