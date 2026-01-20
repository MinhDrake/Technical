from typing import List


class Solution:
    # find the pivot is the total number of rotating, the smallest number in rotated sorted array
    def findPivot(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    def twoPass(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        pivot = self.findPivot(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            midOfRotatedArr = (mid + pivot) % n
            if nums[midOfRotatedArr] == target:
                return midOfRotatedArr
            elif nums[midOfRotatedArr] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    # onePass
    def onePass(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # left array is sorted
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right array is sorted
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


solution = Solution()
nums = [4, 5, 6, 7, 1, 2]
target = 2
print(solution.twoPass(nums, target))
print(solution.onePass(nums, target))

nums1 = [1, 2, 4, 5, 6, 7]
target1 = 2
print(solution.twoPass(nums1, target1))
print(solution.onePass(nums1, target1))

nums2 = [3, 1]
target2 = 1
print(solution.twoPass(nums2, target2))
print(solution.onePass(nums2, target2))
