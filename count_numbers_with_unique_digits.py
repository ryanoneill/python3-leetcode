class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result = 0
        if n == 0:
            result = 1
        else:
            result = 10
            product = 9
            for i in range(2, n + 1):
                result += product * (10 - i + 1)
                product *= 10 - i + 1

        return result
