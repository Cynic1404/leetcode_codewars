
def removeDuplicates(nums):
    k = 0
    checked = set()
    for i in range(len(nums)):
        if nums[i] not in checked:
            checked.add(nums[i])
            nums[k] = nums[i]
            k += 1
    return k


assert removeDuplicates([1,2,3,4,5]) == 5
assert removeDuplicates([]) == 0
assert removeDuplicates([1,2,3,4,5,5,5,5,5,5]) == 5
assert removeDuplicates([1,1,1,1,1,1,5,5,5,5,5]) == 2
