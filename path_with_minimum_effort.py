from collections import deque
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])
        end = (rows-1, columns-1)

        def can_reach_in(effort: int) -> bool:
            result = False

            seen = set()
            queue = deque()
            queue.append((0, 0))
            while queue:
                position = queue.popleft()
                if position == end:
                    result = True
                    break
                else:
                    row, column = position
                    previous = heights[row][column]

                    # Up
                    if row > 0:
                        up = (row-1, column)
                        if up not in seen:
                            diff = abs(previous - heights[up[0]][up[1]])
                            if diff <= effort:
                                seen.add(up)
                                queue.append(up)

                    # Down
                    if row < rows-1:
                        down = (row+1, column)
                        if down not in seen:
                            diff = abs(previous - heights[down[0]][down[1]])
                            if diff <= effort:
                                seen.add(down)
                                queue.append(down)

                    # Left
                    if column > 0:
                        left = (row, column-1)
                        if left not in seen:
                            diff = abs(previous - heights[left[0]][left[1]])
                            if diff <= effort:
                                seen.add(left)
                                queue.append(left)

                    # Right
                    if column < columns-1:
                        right = (row, column+1)
                        if right not in seen:
                            diff = abs(previous - heights[right[0]][right[1]])
                            if diff <= effort:
                                seen.add(right)
                                queue.append(right)

            return result


        left = 0
        right = 10_000_000
        result = 10_000_000
        while left <= right:
            mid = left + (right - left) // 2
            if can_reach_in(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
