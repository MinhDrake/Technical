# https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=efe7b4us

class Solution:
    # remainder
    def reverse(self, x: int) -> int:
        res = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        signed = 1 if x > 0 else -1
        x = x * signed
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
            if res > MAX_INT:
                return 0
            if res < MIN_INT:
                return 0

        return res * signed

    # convertToString
    def convertToString(self, x: int) -> int:
        res = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])

        if res > MAX_INT or res < MIN_INT:
            return 0

        return res


solution = Solution()
# print(solution.reverse(123))
# print(solution.reverse(-123))
# print(solution.reverse(2**31+1))
print(solution.convertToString(-123))
