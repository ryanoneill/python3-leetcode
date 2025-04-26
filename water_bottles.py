class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0

        current = numBottles
        empty = 0
        while current > 0:
            result += current
            empty += current
            current = empty // numExchange
            empty -= (current * numExchange)

        return result

