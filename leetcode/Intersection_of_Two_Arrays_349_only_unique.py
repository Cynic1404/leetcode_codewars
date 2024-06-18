def intersection(nums1, nums2):
    seen = set(nums1)
    res = []
    for i in nums2:
        if i in seen:
            res.append(i)
            seen.remove(i)
    return res
