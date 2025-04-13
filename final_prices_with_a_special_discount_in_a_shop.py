from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        results = [0] * n
        stack = []

        for j, price in enumerate(prices):
            if stack:
                while stack:
                    i = stack[-1]
                    iprice = prices[i]
                    if price <= iprice:
                        stack.pop()
                        discounted = iprice - price
                        results[i] = discounted
                    else:
                        break
            stack.append(j)

        while stack:
            j = stack.pop()
            results[j] = prices[j]

        return results




