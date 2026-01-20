from typing import List
from collections import defaultdict


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)

        if n == k:
            return max(nums)

        for i in range(n - k + 1):
            for j in range(k):
                freq[nums[i+j]] += 1

        res = -1
        for num, count in freq.items():
            if count == 1:
                res = max(res, num)

        return res


solution = Solution()
print(solution.largestInteger([0, 0], 2))
# print(solution.largestInteger([3, 9, 7, 2, 1, 7], 4))
