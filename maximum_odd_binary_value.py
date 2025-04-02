class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = 0
        for d in s:
            if d == "1":
                ones += 1

        result = "1" * (ones - 1) + "0" * (n - ones) + "1"
        return result

