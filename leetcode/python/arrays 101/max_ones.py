from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    max_ones = 0
    results = []

    for idx, n in enumerate(nums):
        if n == 0:
            results.append(max_ones)
            max_ones = 0
        max_ones += n

    results.append(max_ones)
    return max(results)


if __name__ == '__main__':
    print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
