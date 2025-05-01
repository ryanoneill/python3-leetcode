from collections import deque
from typing import List

class Solution:
    def canAssign(self, num: int, tasks: List[int], workers: List[int], pills: int, strength: int) -> bool:
        result = True

        m = len(workers)

        queue = deque()

        windex = m-1
        for i in reversed(range(num)):
            while windex >= (m - num):
                worker = workers[windex]
                if worker + strength >= tasks[i]:
                    queue.append(worker)
                    windex -= 1
                else:
                    break

            if queue:
                if queue[0] >= tasks[i]:
                    queue.popleft()
                elif pills > 0:
                    pills -= 1
                    queue.pop()
                else:
                    result = False
                    break
            else:
                result = False
                break

        return result


    
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        result = 0

        n = len(tasks)
        m = len(workers)

        tasks.sort()
        workers.sort()

        left = 1
        right = min(m, n)
        while left <= right:
            mid = left + (right - left) // 2
            if self.canAssign(mid, tasks, workers, pills, strength):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

