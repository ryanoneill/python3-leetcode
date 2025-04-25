from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        n = len(arr)
        for i in range(0, n - 2):
            inum = arr[i]
            for j in range(i + 1, n - 1):
                jnum = arr[j]
                if abs(inum - jnum) <= a:
                    for k in range(j + 1, n):
                        knum = arr[k]
                        added = abs(jnum - knum) <= b
                        added = added and abs(inum - knum) <= c
                        if added:
                            result += 1

        return result
