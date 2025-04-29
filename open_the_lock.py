from collections import deque
from typing import List

class Solution:
    def up(self, code: str, index: int) -> str:
        digits = [int(digit) for digit in code]
        digits[index] = (digits[index] + 1) % 10
        return "".join(str(digit) for digit in digits)

    def down(self, code: str, index: int) -> str:
        digits = [int(digit) for digit in code]
        digits[index] = (digits[index] - 1) % 10
        return "".join(str(digit) for digit in digits)

    def openLock(self, deadends: List[str], target: str) -> int:
        result = -1 

        queue = deque[str]()
        deadset = set(deadends)
        seen = set()

        moves = 0
        start = "0000"
        if start not in deadset:
            queue.append(start)
            seen.add(start)

        while queue:
            n = len(queue)
            for _ in range(n):
                value = queue.popleft()
                if value == target:
                    result = moves
                    break
                else:
                    for i in range(4):
                        up = self.up(value, i)
                        if up not in seen and up not in deadends:
                            seen.add(up)
                            queue.append(up)
                        down = self.down(value, i)
                        if down not in seen and down not in deadends:
                            seen.add(down)
                            queue.append(down)

            moves += 1

        return result
