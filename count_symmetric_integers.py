# TODO: Implement a Digit DP solution for practice
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            if n % 2 == 0:
                m = n // 2
                first = sum(int(val) for val in s[:m])
                second = sum(int(val) for val in s[m:])
                if first == second:
                    result += 1

        return result
