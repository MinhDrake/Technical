from typing import List


class Solution:
    # way
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = float('-inf'), 0
        for stock in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            cur_hold = max(prev_hold, prev_not_hold - stock)
            cur_not_hold = max(prev_not_hold, prev_hold + stock)

        return cur_not_hold


solution = Solution()
print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# print(solution.maxProfit([1, 2, 3, 4, 5]))
