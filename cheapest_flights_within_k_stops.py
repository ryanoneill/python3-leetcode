from heapq import heappush, heappop
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

        heap = []

        heappush(heap, (0, 0, src))
        while heap:
            hop, price, city = heappop(heap)
            print(hop, price, city)
            if cheapest[city] == -1 or price < cheapest[city]:
                cheapest[city] = price
                if hop < legs and city in hops:
                    for hop_to, hop_price in hops[city].items():
                        heappush(heap, (hop+1, price+hop_price, hop_to))

        return cheapest[dst]
