from typing import List


class Solution:
    """
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1
    """

    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while first <= last:
            idx = (first + last) // 2
            middle = nums[idx]

            if middle < target:
                first = idx + 1
            elif middle > target:
                last = idx - 1
            else:
                return idx
        return -1


if __name__ == '__main__':
    sol = Solution()
    answer = sol.search(nums=[-1,0,3,5,9,12], target=9)
    print(answer)
