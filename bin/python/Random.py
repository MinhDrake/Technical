# https://leetcode.com/problems/implement-rand10-using-rand7/description/?envType=problem-list-v2&envId=efe7b4us
import time


class Solution:
    def rand10(self):
        while True:
            x = (rand7() - 1)*7 + rand7()
            if x <= 40:
                return x % 10


solution = Solution()
print(solution.rand10())
