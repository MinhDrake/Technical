# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
from typing import List
import math

'''
n is length of nums
If we remove zero element, the result is nums[n-1] - nums[0]
If we remove one element, the result is min(the second max nums - the min nums,the max nums -  the second min nums )
so in case 4 elements, we have 4 strategies:
+ Remove 3 biggest elements
+ Remove two biggest elements, one smallest element
+ Remove one biggest element, two smallest elements
+ Remove 3 smallest elements
'''


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        n = len(nums)
        return min(nums[n-4] - nums[0], nums[n-3] - nums[1], nums[n-2] - nums[2], nums[n-1] - nums[3])

    def minDifference2(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        return min(abs(b-a) for a, b in zip(nums[-4:], nums[:4]))


solution = Solution()
print(solution.minDifference2([1, 2, 3, 4, 4, 5, 6, 8, 9]))
