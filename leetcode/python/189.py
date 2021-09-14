from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == len(nums) or not nums:
            return
        l, result = len(nums), [0] * len(nums)
        for idx, n in enumerate(nums):
            result[(idx + k) % l] = nums[idx]
        for idx in range(l):
            nums[idx] = result[idx]


if __name__ == '__main__':
    s = Solution()
    nums, k = [1, 2, 3, 4, 5, 6, 7], 2
    s.rotate(nums, k)
    print(nums)
