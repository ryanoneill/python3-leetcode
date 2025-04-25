class Solution:
    def countEven(self, num: int) -> int:
        result = 0
        for value in range(1, num + 1):
            total = sum((int(num) for num in str(value)))
            if total % 2 == 0:
                result += 1

        return result
