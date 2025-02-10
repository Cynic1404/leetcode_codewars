class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        res=window_sum = 0
        for i in range(k):
            window_sum+=arr[i]

        if window_sum//k>=threshold:
            res+=1

        for i in range(k, len(arr)):
            window_sum+=arr[i]
            window_sum-=arr[i-k]
            if window_sum//k>=threshold:
                res+=1

        return res


