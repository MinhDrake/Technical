# https://leetcode.com/problems/palindrome-partitioning/?envType=problem-list-v2&envId=dynamic-programming
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(result, s, 0, [])
        return result

    def backtrack(self, result: List[List[str]], s: str, start: int, temp_path: List[str]):
        if start == len(s):
            result.append(temp_path[:])
            return

        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                temp_path.append(s[start:end+1])
                self.backtrack(result, s, end+1, temp_path)
                temp_path.pop()

    def is_palindrome(self, s: str, left: int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


solution = Solution()
print(solution.partition("aab"))
