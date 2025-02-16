class Solution:
    def toHex(self, num: int) -> str:
        digits = []
        if num == 0:
            digits.append(str(0))
        else:
            if num < 0:
                num += pow(2, 32)

            while num > 0:
                value = num % 16
                num = num // 16
                digit = str(value)
                if value == 10:
                    digit = "a"
                elif value == 11:
                    digit = "b"
                elif value == 12:
                    digit = "c"
                elif value == 13:
                    digit = "d"
                elif value == 14:
                    digit = "e"
                elif value == 15:
                    digit = "f"
                digits.append(digit)
        result = "".join(reversed(digits))
        return result
