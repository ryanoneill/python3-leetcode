from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []

        n = len(nums)

        for i in range(k):
            value = nums[i]
            counts[value] = counts.get(value, 0) + 1

        result.append(len(counts))

        for j in range(k, n):
            left = j - k
            old = nums[left]
            if counts[old] == 1:
                del counts[old]
            else:
                counts[old] = counts.get(old) - 1

            value = nums[j]
            counts[value] = counts.get(value, 0) + 1
            result.append(len(counts))

        return result
