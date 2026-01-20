# https://leetcode.com/problems/stone-game/
from typing import List
'''
Example we have 5 4 5 3 1 3 - even piles - total 21 is odd so we must have at least one person win
with index      0 1 2 3 4 5 

sumEven: 5 + 5 + 1 = 11
sumOdd: 4 + 3 + 3 = 10

sumEven > sumOdd
Alex always can choose to take all even number or all odd number
example even, alex pick 5, bob must pick between  4 and 3, then alex will pick 5 or 1 and remaining like that
if odd, alex will pick 3 first, then bob must choose between 5 and 1 and alex will pick 4 or 3 which is odd index.

'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


solution = Solution()
print(solution.stoneGame([5, 3, 4, 5]))
