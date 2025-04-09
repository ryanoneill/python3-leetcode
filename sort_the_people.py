from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        results = [i for i in range(n)]
        results.sort(key=lambda i: -heights[i])
        return [names[i] for i in results]
