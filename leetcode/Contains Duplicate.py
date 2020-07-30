# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for v in range(i + 1, len(nums)):
#             if nums[i] == nums[v]:
#                 return True


def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

print(containsDuplicate([1,2,3,1]))


