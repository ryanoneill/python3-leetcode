from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 10_000_000

        cache = {}
        def worker(index: int, prev_color: int, prev_neighbs: int) -> int:
            result = MAX_COST 
            if index == m:
                result = 0 if prev_neighbs == target else MAX_COST
            elif prev_neighbs > target:
                result = MAX_COST
            else:
                key = (index, prev_color, prev_neighbs)
                if key not in cache:
                    if houses[index] == 0:
                        for color in range(1, n+1):
                            neighbs = prev_neighbs 
                            neighbs += 1 if color != prev_color else 0
                            current = cost[index][color-1]
                            current += worker(index+1, color, neighbs)
                            result = min(result, current)
                    else:
                        color = houses[index]
                        neighbs = prev_neighbs 
                        neighbs += 1 if color != prev_color else 0
                        result = worker(index+1, color, neighbs)
                    cache[key] = result
                result = cache[key]
            return result

        result = worker(0, 0, 0)
        if result == MAX_COST:
            result = -1
        return result

