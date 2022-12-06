from typing import List


class Solution(object):
    def duplicate_zeros(self, arr: List[int]) -> None:
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return
        
        prev = arr[0]
        for idx, el in enumerate(arr):
            if el == 0:
                for i in range(idx + 1, len(arr)):
                    temp = arr[i]
                    if i == idx + 1:
                        arr[i] = 0
                     
            

if __name__ == '__main__':
    s = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    s.duplicate_zeros(arr=arr)
    print(arr)
