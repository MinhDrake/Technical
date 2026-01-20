from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(0, i):
                if j == 0 or j == i-1:
                    temp.append(1)
                else:
                    temp.append(res[i-2][j-1] + res[i-2][j])
            res.append(temp)

        return res

    def generate2(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i+1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res


solution = Solution()
# print(solution.generate(1))
# print(solution.generate(2))
# print(solution.generate(5))
print(solution.generate2(5))
