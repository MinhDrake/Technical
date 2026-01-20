class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.checkIfMatch(s, 0, p, 0)

    def checkIfMatch(self, s: str, sidx: int, p: str, pidx: int) -> bool:
        if pidx >= len(p):
            if len(s) == sidx:
                return True
            return False

        if pidx + 1 < len(p) and p[pidx+1] == '*':
            if sidx < len(s) and (p[pidx] == '.' or p[pidx] == s[sidx]):
                return self.checkIfMatch(s, sidx+1, p, pidx)
            else:
                return self.checkIfMatch(s, sidx, p, pidx+2)

        if sidx < len(s) and (p[pidx] == '.' or p[pidx] == s[sidx]):
            return self.checkIfMatch(s, sidx+1, p, pidx+1)

        return False


solution = Solution()
print(solution.isMatch("aa", "aa"))
print(solution.isMatch("aba", "a.*"))
print(solution.isMatch("aaaaaa", "ab."))
print(solution.isMatch("ab", "a.bachac"))
print(solution.isMatch("aa", "a"))
print(solution.isMatch("aab", "c*a*b"))
print(solution.isMatch("ab", ".*c"))
