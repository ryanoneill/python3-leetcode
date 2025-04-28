from heapq import heappush, heappop
from collections import deque
from typing import List, Tuple
from operator import methodcaller

class Task:
    def __init__(self, enqueue_time: int, processing_time: int, index: int) -> None:
        self.enqueue_time = enqueue_time
        self.processing_time = processing_time
        self.index = index

    def by_enqueue(self) -> Tuple[int, int, int]:
        return (self.enqueue_time, self.processing_time, self.index)

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        results = []

        queue = deque(
            sorted((Task(item[0], item[1], i) for i, item in enumerate(tasks)),
            key=methodcaller('by_enqueue')))
        heap = []

        time = 0
        while queue or heap:
            while queue:
                if queue[0].enqueue_time <= time:
                    task = queue.popleft()
                    heappush(heap, (task.processing_time, task.index))
                elif not heap:
                    time = queue[0].enqueue_time
                else:
                    break

            if heap:
                processing_time, index = heappop(heap)
                results.append(index)
                time += processing_time

        return results

