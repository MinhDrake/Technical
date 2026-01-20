from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(0, 0, "", result, n)
        return result

    def dfs(self, left: int, right: int, temp: str, result: List[str], n: int):
        if len(temp) == n*2:
            result.append(temp)
            return

        if left < n:
            self.dfs(left+1, right, temp + '(', result, n)

        if right < left:
            self.dfs(left, right + 1, temp + ')', result, n)


solution = Solution()
print(solution.generateParenthesis(3))
