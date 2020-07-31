def singleNumber(nums):
    counter = 0
    nums = sorted(nums)
    while counter<len(nums)-1:
        if nums[counter] != nums[counter + 1]:
            return nums[counter]
        else:
            counter += 2
    return nums[counter]

print(singleNumber([4,1,2,1,2,5,5,7,7,4,9]))