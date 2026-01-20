# https://leetcode.com/contest/weekly-contest-415/problems/the-two-sneaky-numbers-of-digitville/
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        exist = set()
        res = []

        for num in nums:
            if num in exist:
                res.append(num)
                if res.count == 2:
                    return res
            exist.add(num)

        return res


# test
solution = Solution()
nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
print(solution.getSneakyNumbers(nums))
