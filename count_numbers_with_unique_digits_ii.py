class Solution:
    def numberCount(self, a: int, b: int) -> int:
        result = 0
        for num in range(a, b + 1):
            s = str(num)
            values = set(s)
            if len(s) == len(values):
                result += 1

        return result
