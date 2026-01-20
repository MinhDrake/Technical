def merge(self, nums1, m, nums2, n):
  for j in range(n):
    nums[m+j] = nums2[j]
  nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)