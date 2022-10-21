def arithmeticTriplets(nums, diff):
    checker = {}
    sum_pairs = []
    count = 0

    # use the 'two-sum' solution approach to find all pairs and save their pairs of indexes
    for i in range(len(nums)):
        if nums[i] - diff not in checker:
            checker[nums[i]] = i
        else:
            sum_pairs.append([checker[nums[i] - diff], i])
            checker[nums[i]] = i

    # check if second element of one pair equals first element of another pair
    for first_pair in range(len(sum_pairs)):
        for second_pair in range(first_pair + 1, len(sum_pairs)):
            if sum_pairs[first_pair][1] == sum_pairs[second_pair][0]:
                count += 1
    return count


print(arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))