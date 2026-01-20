# https://leetcode.com/problems/longest-palindromic-substring/

# a string is considered a palindrome substring if its revert equals to its origin.
class Solution:
    # time complexity: O(nC2 *  n) -> O(n3)
    # space complexity: O91
    def bruteForce(self, s: str) -> str:
        res = s[0]
        longest = 1
        for i in range(0, len(s) - 1):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and (j - i + 1) > longest:
                    res = s[i:j+1]
                    longest = j-i + 1
        return res

    # expand string
    def expand_from_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def expandStr(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        result = s[0]
        for i in range(len(s) - 1):
            odd_len = self.expand_from_center(s, i, i)
            even_len = self.expand_from_center(s, i, i+1)

            if odd_len > max_len:
                max_len = odd_len
                result = s[i - (odd_len - 1) // 2:i + (odd_len - 1) // 2 + 1]
            if even_len > max_len:
                max_len = even_len
                result = s[i - (even_len - 2) // 2:i + 1 +
                           (even_len - 2) // 2 + 1]

        return result

    # dynamic programming
    def dp_table(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 0
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if (s[i] == s[j] and (i - j + 1 < 3 or dp[j+1][i-1])):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j:i+1]
        return max_str


solution = Solution()
s = "ababa"
# print(solution.bruteForce(s))
# print(solution.expandStr(s))
print(solution.dp_table(s))
