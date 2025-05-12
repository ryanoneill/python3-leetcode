from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        results = []
        counts = Counter(digits)
        for num in range(100, 1000, 2):
            result = True
            current = Counter(map(int, str(num)))
            for key in current.keys():
                if key not in counts:
                    result = False
                    break
                elif current[key] > counts[key]:
                    result = False
                    break
            if result:
                results.append(num)
        return results


