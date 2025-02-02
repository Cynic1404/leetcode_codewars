
#sliding window
def maximumUniqueSubarray(nums):
    res = left = curr = 0
    seen = set()
    for right in range(len(nums)):
        while nums[right] in seen:
            curr -= nums[left]
            seen.remove(nums[left])
            left += 1

        curr += nums[right]
        res = max(res, curr)
        seen.add(nums[right])
    return res


#hasMap
# from collections import defaultdict
# def maximumUniqueSubarray(nums):
#     res = left = curr = 0
#     seen = defaultdict(int)
#
#     for right in range(len(nums)):
#         if nums[right] in seen:
#             temp_left = seen[nums[right]]+1
#             while left<temp_left:
#                 curr-=nums[left]
#                 left+=1
#
#         curr += nums[right]
#         res = max(res, curr)
#         seen[nums[right]]=right
#
#     return res

assert maximumUniqueSubarray([4,2,4,5,6]) == 17
assert maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]) == 8