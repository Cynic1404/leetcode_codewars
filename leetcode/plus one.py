def plusOne(digits):
    for i in range(len(digits)):
        idx = len(digits) - 1 - i
        # set all the nines at the end of array to zeros
        if digits[idx] == 9:
            digits[idx] = 0
        # here we have the rightmost not-nine
        else:
            # increase this rightmost not-nine by 1
            digits[idx] += 1
            # and the job is done
            return digits
    return [1] + digits


print(plusOne([9,9,9,9]))


#python solution

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         res = ''
#         for i in digits:
#             res += str(i)
#         res = str(int(res) + 1)
#         return list(res)