def intersect(nums1, nums2):
    checker = {}
    if len(nums1) <= len(nums2):
        shorter_list, longer = nums1, nums2
    else:
        shorter_list, longer = nums2, nums1
    for i in shorter_list:
        if i in checker:
            checker[i] = checker[i] + 1
        else:
            checker[i] = 1
    res = []
    for i in longer:
        if i in checker and checker[i] > 0:
            checker[i] = checker[i] - 1
            res.append(i)

    return res