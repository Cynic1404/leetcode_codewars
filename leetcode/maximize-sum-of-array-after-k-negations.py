def largestSumAfterKNegations(nums, k):
    z = sorted(enumerate(nums), key=lambda x: x[1])[:k]
    negative = []
    for i in z:
        if i[1] < 0:
            negative.append(i[0])
        elif i[1] == 0:
            for index_to_replace in negative:
                nums[index_to_replace] = -nums[index_to_replace]
            return sum(nums)

    #find min abs
    min_abs_index = 0
    min_number = abs(nums[0])
    for i in range(1, len(nums)):
        if abs(nums[i]) < min_number:
            min_number = abs(nums[i])
            min_abs_index = i

    for i in negative:
        nums[i] = -nums[i]
    if (k - len(negative)) % 2 == 0:
        return sum(nums)
    nums[min_abs_index] = -nums[min_abs_index]
    return sum(nums)