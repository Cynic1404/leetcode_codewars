def canBeIncreasing(nums):
    if len(nums) <= 2:
        return True
    for i in range(len(nums) - 2):
        if nums[i] >= nums[i + 1]:
            if nums[i] >= nums[i + 2]:
                del (nums[i])
                start_index = 0 if i >= 0 else i - 1
            elif nums[i] < nums[i + 2]:
                del (nums[i + 1])
                start_index = i
            for v in range(start_index, len(nums) - 1):
                if nums[v] >= nums[v + 1]:
                    return False
    return True


print(canBeIncreasing([23,297,427,949,945]))
print(canBeIncreasing([1, 2, 10, 5, 7]))
print(canBeIncreasing([105, 924, 32, 968]))
print(canBeIncreasing([100, 21, 100]))
print(canBeIncreasing([1, 1, 1]))
print(canBeIncreasing([2, 3, 1, 2]))
