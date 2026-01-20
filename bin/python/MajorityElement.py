from typing import List
# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
