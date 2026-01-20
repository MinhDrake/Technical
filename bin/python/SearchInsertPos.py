# https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=array
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))


nums1 = [1, 3, 5, 6]
target1 = 7
print(solution.searchInsert(nums1, target1))
