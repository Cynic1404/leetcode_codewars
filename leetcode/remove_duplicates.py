def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = 0
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        print(nums[i],nums[counter])
        if nums[i] != nums[counter]:
            counter += 1
            nums[counter] = nums[i]
    return counter + 1



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))