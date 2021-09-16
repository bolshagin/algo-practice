from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        l, m = len(s) - 1, len(s) // 2
        for idx in range(m):
            last, t = l - idx, s[idx]
            s[idx] = s[last]
            s[last] = t


if __name__ == '__main__':
    s = Solution()
    xs = [x for x in 'hello']
    s.reverse_string(xs)
    print(xs)
