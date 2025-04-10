class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(num) for num in str(n)]
        result = 0
        pos = True

        for digit in digits:
            if pos:
                result += digit
            else:
                result -= digit
            pos = not pos

        return result
