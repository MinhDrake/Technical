class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]

        # Base case: A single character is always a palindrome
        for i in range(n):
            for c in range(k+1):
                dp[i][i][c] = 1

        # Fill dp table for substrings of increasing length
        for length in range(2, n+1):  # length of substring
            for i in range(n-length+1):
                j = i + length - 1
                for c in range(k+1):
                    # Case 1: If characters match, extend the palindrome
                    if s[i] == s[j]:
                        dp[i][j][c] = 2 + dp[i+1][j-1][c]
                    else:
                        # Case 2: Either remove s[i] or remove s[j]
                        dp[i][j][c] = max(dp[i+1][j][c], dp[i][j-1][c])

                        # Case 3: Replace one of them to make them match
                        if c > 0:
                            # Check if s[i] can be modified to match s[j]
                            if (ord(s[i]) + 1) % 26 == ord(s[j]) % 26 or (ord(s[i]) - 1) % 26 == ord(s[j]) % 26:
                                dp[i][j][c] = max(
                                    dp[i][j][c], 2 + dp[i+1][j-1][c-1])

                            # Check if s[j] can be modified to match s[i]
                            if (ord(s[j]) + 1) % 26 == ord(s[i]) % 26 or (ord(s[j]) - 1) % 26 == ord(s[i]) % 26:
                                dp[i][j][c] = max(
                                    dp[i][j][c], 2 + dp[i+1][j-1][c-1])

        return dp[0][n-1][k]


solution = Solution()
print(solution.longestPalindromicSubsequence("abced", 2))
