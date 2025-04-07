from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        m = len(potions)
        potions.sort()
        print(potions)
        n = len(spells)

        results = [0] * n

        for i in range(n):
            spell = spells[i]

            left = 0
            right = m - 1

            while left <= right:
                mid = left + (right - left) // 2
                potion = potions[mid] * spell
                if potion < success:
                    left = mid + 1
                else:
                    right = mid - 1

            results[i] = m - left

        return results
