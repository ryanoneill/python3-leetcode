from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * n

        for pair in trust:
            truster, trustee = pair

            truster_index = truster - 1
            trusts[truster_index] -= 1

            trustee_index = trustee - 1
            trusts[trustee_index] += 1

        result = -1
        for i in range(n):
            if trusts[i] == n - 1:
                result = i + 1
                break

        return result
