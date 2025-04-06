from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        holding = -prices[0]
        free = 0

        for i in range(1, n):
            price = prices[i]
            previous = holding
            holding = max(holding, free - price)
            free = max(free, previous + price - fee)

        return free
