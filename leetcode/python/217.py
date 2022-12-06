from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = n
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
