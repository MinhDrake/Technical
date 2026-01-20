# https://leetcode.com/problems/zigzag-conversion/description/?envType=problem-list-v2&envId=string
class Solution:
    # time complexity: O(n)
    # space complexity: O(n) - n is len of s
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        nums = [""] * numRows
        curr_row = 0
        direction = 1

        for c in s:
            nums[curr_row] += c
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1
            curr_row += direction

        return "".join(nums)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))
