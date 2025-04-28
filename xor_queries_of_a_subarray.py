from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)

        value = 0
        for i, num in enumerate(arr):
            value ^= num
            prefix[i+1] = value

        results = []
        for query_from, query_to in queries:
            result = prefix[query_from] ^ prefix[query_to+1]
            results.append(result)

        return results
