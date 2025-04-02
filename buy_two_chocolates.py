from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_one = -1
        min_two = -1

        for i, price in enumerate(prices):
            if min_one == -1:
                min_one = i
            elif min_two == -1:
                if price < prices[min_one]:
                    min_two = min_one
                    min_one = i
                else:
                    min_two = i
            else:
                if price < prices[min_one]:
                    min_two = min_one
                    min_one = i
                elif price < prices[min_two]:
                    min_two = i

        cost = prices[min_one] + prices[min_two]
        result = money
        if cost <= money:
            result -= cost
        return result
