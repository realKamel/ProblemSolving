from collections import deque
from typing import Deque


class Solution:
    # Time Complexity O(1)
    def intToRoman(self, num: int) -> str:
        ref = {
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
            1: "I",
        }
        roman_string = ""
        # this loop is fixed-sized 13 iterations is executed
        for key, value in ref.items():
            temp = num // key
            if temp != 0:
                roman_string += value * temp
                num = num % key
        return roman_string


result = Solution().intToRoman(3749)
