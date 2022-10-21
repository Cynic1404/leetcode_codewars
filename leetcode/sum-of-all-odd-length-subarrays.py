def sumOddLengthSubarrays(arr):
    count = 0
    subarr_len = 1
    while subarr_len<=len(arr)+1:
        for i in range(len(arr)):
            if i+subarr_len>len(arr):
                break
            opa = arr[i:i+subarr_len]
            count+=sum(opa)

        subarr_len+=2
    return count


print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))

# brute force
# def sumOddLengthSubarrays(arr):
#     count = 0
#     for i in range(len(arr)+1):
#         for v in range(i+1, len(arr)+1):
#             if len(arr[i:v])%2!=0:
#                 count+=sum(arr[i:v])
#     return count