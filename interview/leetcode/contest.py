class Solution:
    # not sort
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = {}
        ans = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] <= k:
                ans.append(num)
        return ans

    def limitOccurencesInPlace(self, nums: list[int], k: int) -> list[int]:
        left = 0
        for right in range(len(nums)):
            if left < k or nums[right] != nums[left - k]:
                nums[left] = nums[right]
                left += 1
        return nums[:left]


sol = Solution()
print(sol.limitOccurencesInPlace([1, 1, 1, 2, 2, 3], 2))
