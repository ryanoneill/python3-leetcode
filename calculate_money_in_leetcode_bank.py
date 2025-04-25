class Solution:
    def totalMoney(self, n: int) -> int:
        rem = n % 7
        weeks = n // 7
        result = 0

        for i in range(1, weeks + 1):
            result += 28 + (i - 1) * 7

        start = weeks + 1
        for i in range(rem):
            result += start + i

        return result
