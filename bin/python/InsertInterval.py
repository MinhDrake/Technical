from tracemalloc import start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, start, end = 0, newInterval[0], newInterval[1]
        n = len(intervals)
        res = []

        while idx < n and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1

        # combine with the equal
        while idx < n and newInterval[1] >= intervals[idx][0]:
            start = min(start, intervals[idx][0])
            end = max(end, intervals[idx][1])
            idx += 1

        res.append([start, end])

        while idx < n:
            res.append(intervals[idx])
            idx += 1

        return res


solution = Solution()
# print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # output: [[1,5],[6,9]]
# print(solution.insert([[1, 3], [6, 9]], [10, 12]))  # output: [[1,5],[6,9]]
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
