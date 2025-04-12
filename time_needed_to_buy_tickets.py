from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        buying = tickets[k]

        for i, count in enumerate(tickets):
            if i < k:
                result += min(count, buying)
            elif i == k:
                result += buying
            else:
                result += min(count, buying-1)

        return result
