from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        results = []

        by_number = {}
        by_color = {} 

        for query in queries:
            num = query[0]
            color = query[1]

            if num in by_number:
                previous = by_number[num]
                if by_color[previous] == 1:
                    del by_color[previous]
                else:
                    by_color[previous] -= 1
            by_number[num] = color
            if color not in by_color:
                by_color[color] = 1 
            else:
                by_color[color] += 1

            results.append(len(by_color))

        return results
