from tempfile import tempdir
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        first, second = -1, -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                first = i-1
                break
        if first == -1:
            nums.reverse()
            return

        for j in range(len(nums) - 1, first, -1):
            if nums[j] > nums[first]:
                second = j
                break

        nums[first], nums[second] = nums[second], nums[first]

        nums[first+1:] = reversed(nums[first+1:])


solution = Solution()
# nums = [1, 2, 3]
# solution.nextPermutation(nums)
# print(nums)

nums1 = [1, 3, 2]
solution.nextPermutation(nums1)
print(nums1)
