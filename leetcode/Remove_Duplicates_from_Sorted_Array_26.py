
# def removeDuplicates(nums):
#     k = 0
#     checked = set()
#     for i in range(len(nums)):
#         if nums[i] not in checked:
#             checked.add(nums[i])
#             nums[k] = nums[i]
#             k += 1
#     return k

# def removeDuplicates(nums):
#     left=1
#     for right in range(1, len(nums)):
#         if nums[left-1]!=nums[right]:
#             nums[left]=nums[right]
#             left+=1
#     return left

def removeDuplicates(nums):
    left=1
    for right in range(1, len(nums)):
        if nums[right]>nums[right-1]:
            nums[left]=nums[right]
            left+=1
    return left

# assert removeDuplicates([1,2,3,4,5]) == 5
#assert removeDuplicates([]) == 0 works with the first solution only
assert removeDuplicates([0,0,0,1,1,1,2,2,3,3,4]) == 5
assert removeDuplicates([1,1,1,1,1,1,5,5,5,5,5]) == 2
