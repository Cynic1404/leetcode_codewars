# def missingNumber(nums):
#     nums = sorted(nums)
#     for i in range(len(nums)):
#         if i != nums[i]:
#             return i
#     return i+1


def missingNumber(nums):
    s = sum([i for i in range(len(nums)+1)])
    for i in nums:
        s-=i
    return s

print(missingNumber([0]))