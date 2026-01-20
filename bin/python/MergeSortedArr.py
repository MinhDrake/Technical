from typing import List
# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos = len(nums1)
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[pos-1] = nums1[m-1]
                m -= 1
            else:
                nums1[pos-1] = nums2[n-1]
                n -= 1
            pos -= 1

        while m > 0:
            nums1[pos-1] = nums1[m-1]
            pos -= 1
            m -= 1
        while n > 0:
            nums1[pos-1] = nums2[n-1]
            pos -= 1
            n -= 1
