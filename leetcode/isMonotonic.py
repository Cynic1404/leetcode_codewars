def isMonotonic(nums) -> bool:
    if len(nums) == 1 or (len(nums) == 2 and nums[0] != nums[1]):
        return True
    else:
        i=0
        while i < len(nums):
            if nums[i]!=nums[i+1]:
                if nums[i]<nums[i+1]:
                    for v in range(i+1, len(nums)-1):
                        if nums[v]>nums[v+1]:
                            return False
                elif nums[i]>nums[i+1]:
                    for v in range(i+1, len(nums)-1):
                        if nums[v]<nums[v+1]:
                            return False
                return True
            else:
                i+=1
        return True


#
print(isMonotonic([1,1,1]))