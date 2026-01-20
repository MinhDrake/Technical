from operator import le
from typing import List



class Solution:
    def sort(self, nums: List[int]) -> None:
        self.quickSort(nums, 0, len(nums) - 1)

    def swap(self, nums: List[int], left: int, right: int) -> None:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        pivot = nums[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.quickSort(nums, left, j)
        self.quickSort(nums, i, right)


solution = Solution()
nums = [2, 1, 0, 1, 2, 0]
solution.sort(nums)
print(nums)
