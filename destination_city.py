from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        overall = set()

        for path in paths:
            city_from, city_to = path

            outgoing.add(city_from)

            overall.add(city_from)
            overall.add(city_to)

        diff = overall.difference(outgoing)
        return diff.pop()
