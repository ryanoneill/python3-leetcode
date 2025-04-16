class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0
        if low % 2 == 1:
            result = (high - low) // 2 + 1
        else:
            result = (high + 1 - low) // 2
        return result
