from typing import List
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m == 1:
            return sum(grid[0])

        if n == 1:
            return sum(grid[r][0] for r in range(m))

        def maxRange(sub_arr: List[int]) -> int:
            curr1 = sub_arr[0]
            curr2 = -float("inf")
            ans = -float("inf")

            for i in range(1,len(sub_arr)):
                curr2 = max(curr2 + sub_arr[i], curr1 + sub_arr[i])
                curr1 = max(curr1 + sub_arr[i], sub_arr[i])

                ans = max(ans, curr2)

            return ans
        ans = -float('inf')
        for i in range(m):
            ans = max(ans, maxRange(grid[i]))

        for j in range(n):
            ans = max(ans, maxRange([grid[r][j] for r in range(m)]))
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans = max(ans, grid[i][j])
        return ans

sol = Solution()
print(sol.maxScore([[-17,-3,-14,3,-10,-18,2,-5],[-19,8,4,-13,-1,13,-13,8],[5,4,-18,4,-13,-11,4,-15]]))