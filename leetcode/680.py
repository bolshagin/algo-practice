class Solution:
    def valid_palindrome(self, s: str) -> bool:
        l = len(s) - 1
        more = []

        for i in range(l // 2):
            if s[i] != s[l - i]:
                more.append(s[i])
        print(more)
        return len(more) < 2


if __name__ == '__main__':
    s = Solution()
    print(s.valid_palindrome('abc'))
