
def removeDuplicates(nums):
    o = 0
    while o+1 < len(nums):
        if nums[o] == nums[o+1]:
            del nums[o+1]
        else:
            o+=1
    return len(nums)


assert removeDuplicates([1,2,3,4,5]) == 5
assert removeDuplicates([]) == 0
assert removeDuplicates([1,2,3,4,5,5,5,5,5,5]) == 5
assert removeDuplicates([1,1,1,1,1,1,5,5,5,5,5]) == 2
