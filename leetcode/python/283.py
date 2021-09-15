from typing import List


class Solution:
    def move_zeros(self, nums: List[int]) -> None:
        result = []
        for n in nums:
            if n != 0:
                result.append(n)

        for idx, n in enumerate(nums):
            if idx < len(result):
                nums[idx] = result[idx]
            else:
                nums[idx] = 0


if __name__ == '__main__':
    s = Solution()
    nums = [0]
    s.move_zeros(nums=nums)
    print(nums)
