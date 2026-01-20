class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = roman_dict[s[0]]
        for i in range(1, len(s)):
            if roman_dict[s[i-1]] < roman_dict[s[i]]:
                res = res - 2*roman_dict[s[i-1]] + roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]

        return res


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("IV"))
print(solution.romanToInt("MDCC"))
