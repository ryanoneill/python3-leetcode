import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = False
        if num > 1:
            upper = int(math.sqrt(num))
            divisor_sum = 1
            for i in range(2, upper + 1):
                if num % i == 0:
                    divisor_sum += i
                    j = num // i
                    if j != i:
                        divisor_sum += j

            result = num == divisor_sum
        return result
