class Solution:
    def __init__(self, bad: int):
        self.bad = bad

    def first_bad_version(self, n: int) -> int:
        first, last = 1, n
        while first < last:
            version = (first + last) // 2
            if self.is_bad_version(version):
                last = version
            else:
                first = version + 1
        return last

    def is_bad_version(self, version: int) -> bool:
        return version >= self.bad


if __name__ == '__main__':
    sol = Solution(bad=2)
    answer = sol.first_bad_version(n=2)
    print(answer)
