from collections import deque
from typing import Dict, List

class Solution:
    def flights_to_hops(self, flights: List[List[int]]) -> Dict[int, Dict[int, int]]:
        result = {}
        for flight_from, flight_to, price in flights:
            if flight_from not in result:
                result[flight_from] = {}
            result[flight_from][flight_to] = price

        return result

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hops = self.flights_to_hops(flights)
        legs = k + 1

        cheapest = [-1 for _ in range(n)]

        queue = deque()
        queue.append((0, 0, src))

        while queue:
            hop, price, city = queue.popleft()
            print(hop, price, city)
            if cheapest[city] == -1 or price < cheapest[city]:
                cheapest[city] = price
                if hop < legs and city in hops:
                    for hop_to, hop_price in hops[city].items():
                        queue.append((hop+1, price+hop_price, hop_to))

        return cheapest[dst]
