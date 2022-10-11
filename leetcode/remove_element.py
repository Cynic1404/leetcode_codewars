
def removeElement(nums, val):
    if nums:
        counter = 0
        removed = 0
        if val in nums:
            while nums[counter] != '_':
                if nums[counter] == val:
                    for i in range(counter, len(nums) - 1):
                        nums[i] = nums[i + 1]
                    nums[-1] = '_'
                    counter -= 1
                    removed += 1
                counter += 1
            return (len(nums) - removed)
        else:
            return nums
    else:
        return 0

print(removeElement([2], 3))