class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(-2, -len(arr)-1, -1):
            if arr[i] == 0:
                for i in range(-1, i, -1):
                    arr[i] = arr[i-1]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(-2, -len(arr)-1, -1):
            if arr[i] == 0:
                arr[i:] = [0]+arr[i:-1]
