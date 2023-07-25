from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for x in range(len(numbers)):
            y = target - numbers[x]
            if y in d:
                return d[y], x
            else:
                d[nums[x]] = x

    def two_sum_bs(self, numbers: List[int], target: int) -> List[int]:
        pass


if __name__ == '__main__':
    s = Solution()
    nums, t = [-1, 0], -1
    ans = s.two_sum(numbers=nums, target=t)
    print(ans)
