from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            s_word = ''.join(sorted(word))
            if s_word in result:
                result[s_word].append(word)
            else:
                result[s_word] = [word]
        return list(result.values())


if __name__ == '__main__':
    s = Solution()
    tests = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"]
    ]
    for test in tests:
        print(s.group_anagrams(test))
