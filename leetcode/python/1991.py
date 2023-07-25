from typing import List


class Solution:
    def find_middle_index(self, nums: List[int]) -> int:
        left, right = [0] * (l := len(nums)), [0] * l
        sum = 0
        for i in range(1, l):
            sum += nums[i - 1]
            left[i] = sum
        sum = 0
        for i in range(l - 2, -1, -1):
            sum += nums[i + 1]
            right[i] = sum
        for i in range(l):
            if left[i] == right[i]:
                return i
        return -1      
        


if __name__ == '__main__':
    s = Solution()
    tests = [
        [[2, 3, -1, 8, 4], 3],
        [[1, 7, 3, 6, 5, 6], 3],
        [[1, 2, 3], -1],
        [[2, 1, -1], 0]
    ]

    for t in tests:
        nums, answer = t[0], t[1]
        assert s.find_middle_index(nums) == answer
