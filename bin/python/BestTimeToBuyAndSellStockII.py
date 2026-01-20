from calendar import c
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     sum = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] > prices[i-1]:
    #             sum += prices[i] - prices[i-1]

    #     return sum

    # # way 2
    # def maxProfit2(self, prices: List[int]) -> int:
    #     cur_hold, cur_not_hold = float('-inf'), 0
    #     for stock in prices:
    #         prev_hold, prev_not_hold = cur_hold, cur_not_hold
    #         cur_hold = max(prev_hold, prev_not_hold - stock)
    #         cur_not_hold = max(prev_not_hold, prev_hold + stock)

    #     return cur_not_hold

    def maxProfit3(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

    # dynamic programming
    # break the problem into two variables (not hold and holding), solving each subproblem and store it
    # to achieve the final result
    # not hold and hold
    # hold[i] = max(hold[i-1], cash[i-1] - prices[i])
    # cash[i] = max(cash[i-1], prices[i] hold[i-1])
    def maxProfit4(self, prices: List[int]) -> int:
        cash, hold = [0]*len(prices), [0]*len(prices)
        cash[0], hold[0] = 0, -prices[0]

        for idx in range(1, len(prices)):
            hold[idx] = max(hold[idx-1], cash[idx-1] - prices[idx])  # holding
            cash[idx] = max(cash[idx-1], prices[idx] +
                            hold[idx-1])  # not holding

        return cash[len(prices)-1]

    # prices.length > 0
    def optimizeMaxProfit4(self, prices: List[int]) -> int:
        cash, hold = 0, - prices[0]

        for idx in range(1, len(prices)):
            prev_cash = cash
            cash = max(cash, hold + prices[idx])
            hold = max(hold, prev_cash - prices[idx])

        return cash


solution = Solution()
# print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
# print(solution.maxProfit([1, 2, 3, 4, 5]))

# print(solution.maxProfit2([7, 1, 5, 3, 6, 4]))
# print(solution.maxProfit2([1, 2, 3, 4, 5]))

# print(solution.maxProfit3([7, 1, 5, 3, 6, 4]))
# print(solution.maxProfit3([1, 2, 3, 4, 5]))

print(solution.optimizeMaxProfit4([7, 1, 5, 3, 6, 4]))
print(solution.optimizeMaxProfit4([1, 2, 3, 4, 5]))
