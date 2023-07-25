from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        num_str = ''.join(str(d) for d in digits)
        num = int(num_str) + 1
        return [int(n) for n in str(num)]


if __name__ == '__main__':
    s = Solution()
    tests = [
        [1, 2, 3],
        [9],
        [4, 3, 2, 1]
    ]
    for test in tests:
        print(s.plus_one(test))