from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]):
        prefix = set()
        for num in arr1:
            while num not in prefix and num > 0:
                prefix.add(num)
                num //=10

        ans = 0
        for num in arr2:
            while num not in prefix and num > 0:
                num //= 10
            if num > 0:
                ans = max (ans, len(str(num)))
        return ans

sol = Solution()
print(sol.longestCommonPrefix([10], [17,11]))