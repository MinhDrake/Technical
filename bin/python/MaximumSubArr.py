from typing import List

# problem: https://leetcode.com/problems/maximum-subarray/description/
# given nums.length >=1


class Solution:

    # brute force - list all subArr
    # O(n2)
    def maxSubArray(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            curr_sub_arr = 0
            for j in range(i, len(arr)):
                curr_sub_arr += arr[j]
                res = max(res, curr_sub_arr)
        return res
    # O(n)

    def maxSubArray2(self, arr: List[int]) -> int:
        res, curr_sub_max = arr[0], 0
        for num in arr:
            curr_sub_max += num
            res = max(res, curr_sub_max)
            if curr_sub_max < 0:
                curr_sub_max = 0

        return res

    def optimizeMaxSubArray2(self, arr: List[int]) -> int:
        res, curr_sub_max = arr[0], arr[0]
        for i in range(1, len(arr)):
            curr_sub_max = max(curr_sub_max + arr[i], arr[i])
            res = max(res, curr_sub_max)

        return res


solution = Solution()
print(solution.maxSubArray([2, 3, -8, 7, -1, 2, 3]))
print(solution.maxSubArray2([2, 3, -8, 7, -1, 2, 3]))
print(solution.optimizeMaxSubArray2([2, 3, -8, 7, -1, 2, 3]))
