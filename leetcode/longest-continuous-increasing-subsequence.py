

# extra requirement!!!!!
#the sequence should increase evenly!!!!

def findLengthOfLCIS(nums):
    if len(nums) == 1:
        return 1
    longest=0
    temp=[]
    diff = None
    for i in range(1, len(nums)):
        if not diff:
            diff = nums[i]-nums[i-1]
            if not diff:
                temp = [nums[i-1]]
            else:
                temp=[nums[i-1], nums[i]]
            longest = max(len(temp), longest)
            continue
        if nums[i]-nums[i-1] == diff:
            temp.append(nums[i])
            longest = max(len(temp), longest)
        else:
            diff = nums[i]-nums[i-1]
            if not diff:
                temp = [nums[i-1]]
            else:
                temp=[nums[i-1], nums[i]]
            longest = max(len(temp), longest)
            continue
    return longest

print(findLengthOfLCIS([1,3,5,4,7]))