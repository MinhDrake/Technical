from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Initialize Prefix DP: prefix[i][j] will store all possible OR values
        # by selecting j elements from the first i elements
        prefix = [[set() for _ in range(k+1)] for _ in range(n+1)]
        prefix[0][0].add(0)  # Base case: OR of 0 elements is 0

        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(0, min(k, i)+1):
                # Case 1: Do not take the current number
                if j <= i-1:
                    prefix[i][j].update(prefix[i-1][j])

                # Case 2: Take the current number
                if j-1 >= 0:
                    for prev_or in prefix[i-1][j-1]:
                        prefix[i][j].add(prev_or | num)

        # Initialize Suffix DP: suffix[i][j] will store all possible OR values
        # by selecting j elements from the last n-i elements
        suffix = [[set() for _ in range(k+1)] for _ in range(n+1)]
        suffix[n][0].add(0)  # Base case: OR of 0 elements is 0

        for i in range(n-1, -1, -1):
            num = nums[i]
            for j in range(0, min(k, n-i)+1):
                # Case 1: Do not take the current number
                if j <= n-i-1:
                    suffix[i][j].update(suffix[i+1][j])

                # Case 2: Take the current number
                if j-1 >= 0:
                    for prev_or in suffix[i+1][j-1]:
                        suffix[i][j].add(prev_or | num)

        max_val = 0
        # Iterate over all possible split points
        for m in range(k, n - k + 1):
            OR_As = prefix[m][k]
            OR_Bs = suffix[m][k]
            # To optimize, iterate through the smaller set first
            if len(OR_As) < len(OR_Bs):
                for or_a in OR_As:
                    for or_b in OR_Bs:
                        max_val = max(max_val, or_a ^ or_b)
            else:
                for or_b in OR_Bs:
                    for or_a in OR_As:
                        max_val = max(max_val, or_a ^ or_b)

        return max_val


# test
nums = [2, 6, 7]
k = 1
solution = Solution()
print(solution.maxValue(nums, k))
