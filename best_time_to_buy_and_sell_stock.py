from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        cost = pow(2, 32) - 1

        for price in prices:
            if price < cost:
                cost = price
            profit = price - cost
            result = max(result, profit)

        return result
