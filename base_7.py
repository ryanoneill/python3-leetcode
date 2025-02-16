class Solution:
    def convertToBase7(self, num: int) -> str:
        result = "0"
        if num != 0:
            digits = []
            negative = num < 0
            if negative:
                num = -num
            while num > 0:
                value = num % 7
                num = num // 7
                digits.append(str(value))
            if negative:
                digits.append("-")
            result = "".join(reversed(digits))
        return result
