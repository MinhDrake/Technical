# https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=dynamic-programming
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(0, len(s) + 1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in wordSet:
                    dp[i] = True

        return dp[len(s)]


solution = Solution()
print(solution.wordBreak("llet", ["l", "et"]))
