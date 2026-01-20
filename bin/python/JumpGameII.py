from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        curr_jump, curr_max, curr_end = 0, 0,  nums[0]
        for i in range(len(nums)):
            curr_max = max(curr_max, i + nums[i])
            if curr_end > len(nums) - 1:
                return curr_jump + 1
            if i == curr_end:
                curr_jump += 1
                curr_end: int = curr_max

        return curr_jump


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))  # 2
print(solution.jump([1, 2, 3]))  # 2
print(solution.jump([0]))  # 0
