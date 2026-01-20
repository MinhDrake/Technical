from os import dup
from typing import List
from collections import defaultdict


class Solution:
    # C1
    def findMissingAndRepeatedValues(self, grid: List[List[int]]):
        char_count = defaultdict(int)
        duplicate_num = 0
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                char_count[grid[i][j]] += 1
                if char_count[grid[i][j]] > 1:
                    duplicate_num = grid[i][j]
                sum += grid[i][j]

        original_sum = pow(len(grid), 2)
        missing_num = original_sum * \
            (original_sum+1) // 2 - (sum - duplicate_num)
        return [duplicate_num, missing_num]

    # C2
    def findMissingAndRepeatedValues2(self, grid: List[List[int]]):
        sum, sqrSum, n, sqrN = 0, 0, len(grid), len(grid)*len(grid)
        for i in range(n):
            for j in range(n):
                sum += grid[i][j]
                sqrSum += grid[i][j] * grid[i][j]

        c1 = sum - sqrN*(sqrN+1) // 2
        c2 = sqrSum - sqrN*(sqrN+1)*(sqrN*2+1) // 6
        return [(c2//c1 + c1) // 2, (c2//c1 - c1) // 2]


solution = Solution()
print(solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
print(solution.findMissingAndRepeatedValues2([[1, 3], [2, 2]]))
