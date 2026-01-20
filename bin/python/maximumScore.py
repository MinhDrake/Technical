# https://leetcode.com/contest/weekly-contest-415/problems/maximum-multiplication-score/description/
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)

        # dp[k] will store the maximum score for choosing k elements
        dp = [-float('inf')] * 5
        dp[0] = 0  # base case, choosing 0 elements has a score of 0

        # Iterate over the array b
        for j in range(n):
            # Iterate backward to update dp for k = 4, 3, 2, 1
            for k in range(4, 0, -1):
                dp[k] = max(dp[k], dp[k-1] + a[k-1] * b[j])

        return dp[4]


# Example usage
a = [3, 2, 5, 6]
b = [2, -6, 4, -5, -3, 2, -7]
solution = Solution()
print(solution.maxScore(a, b))  # Output: 26
