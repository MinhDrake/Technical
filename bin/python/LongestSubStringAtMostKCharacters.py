from collections import defaultdict


class Solution:
    def findLongestSubStrAtMostKCharacters(self, s: str, k: int) -> int:
        start, end, curr_count, res = 0, 0, 0, 0
        char_count = defaultdict(int)
        while end < len(s):
            curr_count += (char_count[s[end]] == 0)
            char_count[s[end]] += 1

            while curr_count > k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    curr_count -= 1
                start += 1

            res = max(res, end - start + 1)
            end += 1
        return res


solution = Solution()
print(solution.findLongestSubStrAtMostKCharacters("eceba", 2))  # 3
print(solution.findLongestSubStrAtMostKCharacters("abcbae", 3))  # 5
print(solution.findLongestSubStrAtMostKCharacters("abc", 0))  # 0
