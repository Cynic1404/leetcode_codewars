
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[left] == 0:
            if nums[right] !=0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        else:
            left+=1

    return nums

print(moveZeroes([1,0,1]))
print(moveZeroes([0,1,0,3,12]))