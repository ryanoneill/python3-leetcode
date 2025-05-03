from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        seen = {}
        for top, bottom in zip(tops, bottoms):
            if top in seen:
                seen[top] += 1
            else:
                seen[top] = 1
            if bottom != top:
                if bottom in seen:
                    seen[bottom] += 1
                else:
                    seen[bottom] = 1
                
        maximum_value = 0
        maximum_count = 0
        for value, count in seen.items():
            if count > maximum_count:
                maximum_value = value
                maximum_count = count

        result = -1
        top_result = 0
        bottom_result = 0
        if maximum_count >= n:
            for top, bottom in zip(tops, bottoms):
                if top != maximum_value:
                    top_result += 1
                if bottom != maximum_value:
                    bottom_result += 1

            result = min(top_result, bottom_result)

        return result




