from typing import List


class Solution:
    def dominant_index(self, nums: List[int]) -> int:
        max, idx = 0, -1
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                idx = i
        for n in nums:
            if max < 2 * n and max != n:
                return -1
        return idx


if __name__ == '__main__':
    s = Solution()
    tests = [
        [3, 6, 1, 0],
        [1, 2, 3, 4]
    ]

    for test in tests:
        print(s.dominant_index(test))