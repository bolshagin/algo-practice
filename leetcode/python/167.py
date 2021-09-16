from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        while first < last:
            sum = numbers[first] + numbers[last]
            if sum == target:
                return [first + 1, last + 1]
            elif sum < target:
                first += 1
            else:
                last -= 1

    def two_sum_bs(self, numbers: List[int], target: int) -> List[int]:
        pass


if __name__ == '__main__':
    s = Solution()
    nums, t = [-1, 0], -1
    ans = s.two_sum(numbers=nums, target=t)
    print(ans)
