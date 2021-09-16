from typing import List


class Solution:
    def reverse_words_pythonic(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])

    def reverse_words(self, s: str) -> str:
        result = []
        for word in s.split():
            result.append(self.reverse_string([w for w in word]))
        return ' '.join(result)

    @staticmethod
    def reverse_string(s: List[str]) -> str:
        l, m = len(s) - 1, len(s) // 2
        for idx in range(m):
            last, t = l - idx, s[idx]
            s[idx] = s[last]
            s[last] = t
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    xs = "Let's take LeetCode contest"
    ans = s.reverse_words(xs)
    print(ans)
