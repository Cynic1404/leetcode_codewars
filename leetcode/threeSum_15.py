
#brute force
# def threeSum(nums):
#     res=[]
#     for f in range(len(nums)-2):
#         for s in range(f+1, len(nums) - 1):
#             if 0 - nums[f]-nums[s] in nums[s+1:]:
#                 if sorted([nums[f],nums[s], 0 - nums[f]-nums[s]]) not in res:
#                     res.append(sorted([nums[f],nums[s],0 - nums[f]-nums[s]]))
#     return res


def threeSum(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right] + nums[i]
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res

print(threeSum(nums=[-1,0,1,2,-1,-4]))