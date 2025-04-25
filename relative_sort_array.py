from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rels = {num: i for i, num in enumerate(arr2)}

        def sortKey(x: int) -> int:
            if x in rels:
                return rels[x]
            else:
                return 2000 + x

        results = sorted(arr1, key=sortKey)
        return results
