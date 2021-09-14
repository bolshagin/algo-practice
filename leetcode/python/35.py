from typing import List


class Solution:
    def search_insert(self, nums: List[int], target) -> int:
        first, last = 0, len(nums) - 1

        if not nums:
            return 0

        while first <= last:
            idx = (first + last) // 2
            middle = nums[idx]

            if middle == target:
                return idx
            elif middle < target:
                first = idx + 1
            elif middle > target:
                last = idx - 1

        return first


if __name__ == '__main__':
    sol = Solution()
    answer = sol.search_insert(nums=[1], target=0)
    print(answer)
