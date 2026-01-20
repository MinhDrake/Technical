from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        left_pos, right_pos = -1, -1

        # find left position
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    right = mid - 1
                else:
                    left_pos = mid
                    break
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        # find right pos
        left = max(0, left_pos)
        right = n - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                if mid < n-1 and nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:
                    right_pos = mid
                    break
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return [left_pos, right_pos]


solution = Solution()
# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(solution.searchRange(nums, target))

# nums1 = [5, 7, 7, 8, 8, 10]
# target1 = 6
# print(solution.searchRange(nums1, target1))

nums2 = []
target2 = 0
print(solution.searchRange(nums2, target2))
