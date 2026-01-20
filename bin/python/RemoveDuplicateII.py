from typing import List


'''
Given two pointers:
wp : write pointer use to write num at specific pos
rp : read pointer use to scans through the array
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        wp = 2  # always take 0 and 1 element
        for rp in range(2, len(nums)):
            if nums[wp-2] != nums[rp]:
                nums[wp] = nums[rp]
                wp += 1

        return wp


solution = Solution()
list = [1, 1, 1, 2, 2, 2, 3]
print(solution.removeDuplicates(list))  # 1,1,2,2,3
print(list)
