from typing import List
from collections import Counter


class Solution:
    def top_k_frequent_pythonic(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        freq = [[] for i in range(len(nums) + 1)]
        for key in d:
            freq[d[key]].append(key)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                for num in freq[i]:
                    if len(result) < k:
                        result.append(num)

        return result


if __name__ == '__main__':
    s = Solution()
    tests = [
        [[1,1,1,2,2,3,3,3,4,4,4,4,4,5], 2],
        [[1], 1],
        [[-1, -1], 1],
        [[1, 2], 2]
    ]

    for test in tests:
        print(s.top_k_frequent(test[0], test[1]))
