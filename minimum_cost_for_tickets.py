from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        cache = {}
        def worker(end: int, index: int) -> int:
            if index == n:
                return 0
            else:
                key = (end, index)
                if key not in cache:
                    result = 0
                    current = days[index]
                    if end >= current:
                        result = worker(end, index+1)
                    else:
                        one_day = costs[0] + worker(current, index+1)
                        seven_day = costs[1] + worker(current+6, index+1)
                        thirty_day = costs[2] + worker(current+29, index+1)
                        result = min(one_day, seven_day, thirty_day)
                    cache[key] = result
                return cache[key]
        return worker(0, 0)
