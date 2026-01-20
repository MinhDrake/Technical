import math


class Solution:
    def intToRoman(self, num: int) -> str:
        if num > 3999:
            return ""
        res = ""
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        nums_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        for value in nums:
            while num >= value:
                res += nums_dict[value]
                num -= value

        return res


solution = Solution()
print(solution.intToRoman(3749))
