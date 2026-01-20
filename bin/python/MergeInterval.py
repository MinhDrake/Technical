from re import I
from typing import List


class Solution:
  #  idea is we loop through array, if we find an overlapping, merge it with the previous
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        res = [intervals[0][:]]  # Do not modify the original array

        for ele in intervals[1:]:
            if ele[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], ele[1])
            else:
                res.append(ele)

        return res


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 12], [10, 12]]))
