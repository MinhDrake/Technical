from typing import List


class Solution:
    # C1: use hashmap to store the colors 's frequency
    def sortColors(self, nums: List[int]) -> None:
        color_count = {}
        for i in range(len(nums)):
            color_count[nums[i]] = color_count.get(nums[i], 0) + 1

        idx = 0
        for color in range(3):
            freq = color_count.get(color, 0)
            nums[idx: idx + freq] = [color] * freq
            idx += freq
    # C2: use three pointer, which includes: red and blue are two pointers position at first and end of the arr.
    # white pointer is using to move step by step

    def sortColors2(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


solution = Solution()
nums = [0, 1, 2, 2, 1, 0]
solution.sortColors(nums)
print(nums)

nums = [2, 1, 1, 0, 0, 2]
solution.sortColors2(nums)
print(nums)
