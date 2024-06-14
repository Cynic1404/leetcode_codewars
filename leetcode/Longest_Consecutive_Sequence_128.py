def longestConsecutive(nums):
    longest = 0
    nums = sorted(nums)
    count = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            count += 1
        elif nums[i] == nums[i - 1]:
            continue
        else:
            count = 0
        longest = max(longest, count)
    if nums:
        return longest + 1
    else:
        return 0

assert longestConsecutive(nums=[0,3,2,5,4,6,1,1]) == 7
assert longestConsecutive(nums = [2,20,4,10,3,4,5]) == 4