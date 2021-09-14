from typing import List


class Solution:
    def sorted_squares_easy(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x * x, nums))


if __name__ == '__main__':
    s = Solution()
    answer = s.sorted_squares_easy(nums=[-4, -1, 0, 3, 10])
    print(answer)
