
def longestConsecutive(nums):
    if not nums:
        return 0

    nums = sorted(nums)
    longest = 0
    counter = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            counter += 1
        elif nums[i] != nums[i - 1]:
            longest = max(longest, counter)
            counter = 1
    return max(longest, counter)

assert longestConsecutive(nums=[]) == 0
assert longestConsecutive(nums=[0,3,2,5,4,6,1,1]) == 7
assert longestConsecutive(nums = [2,20,4,10,3,4,5]) == 4