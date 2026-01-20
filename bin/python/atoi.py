class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        signed = 1
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while idx < len(s) and s[idx] == ' ':
            idx += 1
        if idx < len(s) and (s[idx] == '+' or s[idx] == '-'):
            signed = 1 if s[idx] == '+' else -1
            idx += 1
        while idx < len(s) and s[idx].isnumeric():
            res = res*10 + (int)(s[idx])
            idx += 1

        if signed * res > INT_MAX:
            return INT_MAX
        elif signed * res < INT_MIN:
            return INT_MIN

        return signed * res


solution = Solution()
# s = "42"
# print(solution.myAtoi(s))
# print(solution.myAtoi("-042"))
# print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("-91283472332"))
