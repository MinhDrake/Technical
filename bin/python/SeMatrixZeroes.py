from typing import List


class Solution:
    # O (m+n) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        markZeroes = (len(matrix) + len(matrix[0]))*[1]
        n = len(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    markZeroes[row] = 0
                    markZeroes[n+col] = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] != 0) and (markZeroes[row] == 0 or markZeroes[n+col] == 0):
                    matrix[row][col] = 0
      # O(1) space
      # using flag as matrix[i][0] and matrix[0][j]

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_has_zeros = any(matrix[i][0] == 0 for i in range(m))
        first_col_has_zeros = any(matrix[0][i] == 0 for i in range(n))
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0  # mark row
                    matrix[0][col] = 0  # mark col

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zeros:
            for i in range(0, n):
                matrix[0][i] = 0

        if first_col_has_zeros:
            for i in range(0, m):
                matrix[i][0] = 0


solution = Solution()
# [[1,0,1],[0,0,0],[1,0,1]]
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# solution.setZeroes(matrix)
# print(matrix)

# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# matrix1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# solution.setZeroes(matrix1)
# print(matrix1)

# [[1,0,1],[0,0,0],[1,0,1]]
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# solution.setZeroes1(matrix)
# print(matrix)

# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
matrix1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes1(matrix1)
print(matrix1)
