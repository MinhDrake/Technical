from typing import List
# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 3)
print(nums)
