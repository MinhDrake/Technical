from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        m = len(matrix)
        n = len(matrix[0])

        # transpose
        for i in range(0, m):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # reverse
        for i in range(0, m):
            for j in range(0, n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-j-1] = temp


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution.rotate(matrix))
print(matrix)
