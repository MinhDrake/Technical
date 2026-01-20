from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        curr_len = 0
        frequency = defaultdict(int)

        for i in range(len(s)):
            frequency[s[i]] += 1
            curr_len += 1
            while frequency[s[i]] > 1:
                frequency[s[left]] -= 1
                left += 1
                curr_len -= 1
            res = max(res, curr_len)
        return res


solution = Solution()
s = ""
print(solution.lengthOfLongestSubstring(s))
