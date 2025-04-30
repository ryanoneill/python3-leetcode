from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set(i for i in range(n))

        for _, weaker in edges:
            if weaker in teams:
                teams.remove(weaker)

        result = -1
        if len(teams) == 1:
            result = teams.pop()
        return result
