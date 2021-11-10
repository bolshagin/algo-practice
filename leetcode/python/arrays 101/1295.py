from typing import List


class Solution:
    def find_numbers(self, nums: List[int]) -> int:
        evens_count = 0
        for num in nums:
            digits_count = 1
            while num // 10 > 0:
                num = num // 10
                digits_count += 1
            if digits_count % 2 == 0:
                evens_count += 1
        return evens_count


if __name__ == '__main__':
    s = Solution()
    answer = s.find_numbers(nums=[12, 345, 2, 6, 7896])
    print(answer)
