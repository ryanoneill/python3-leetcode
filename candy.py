from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        counts = [1] * n

        for j in range(1, n):
            i = j - 1
            if ratings[i] < ratings[j]:
                counts[j] = counts[i] + 1

        for i in range(n-2, -1, -1):
            j = i + 1
            if ratings[i] > ratings[j]:
                counts[i] = max(counts[i], counts[j] + 1)

        result = sum(counts)
        return result
            
