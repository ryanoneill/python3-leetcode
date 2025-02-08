from typing import List
from heapq import heappop, heappush

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_order = []
        self.task_items = {}

        for task in tasks:
            user_id = task[0]
            task_id = task[1]
            priority = task[2]

            item = (-priority, -task_id, user_id)
            heappush(self.task_order, item)
            self.task_items[task_id] = item

    def add(self, userId: int, taskId: int, priority: int) -> None:
        item = (-priority, -taskId, userId)
        heappush(self.task_order, item)
        self.task_items[taskId] = item

    def edit(self, taskId: int, newPriority: int) -> None:
        (_, task_id, user_id) = self.task_items[taskId]
        item = (-newPriority, task_id, user_id)
        heappush(self.task_order, item)
        self.task_items[taskId] = item

    def rmv(self, taskId: int) -> None:
        del self.task_items[taskId]

    def execTop(self) -> int:
        result = -1
        while self.task_order:
            item = heappop(self.task_order)
            task_id = item[1] * -1
            if task_id in self.task_items and self.task_items[task_id] == item:
                del self.task_items[task_id]
                result = item[2]
                break
        return result


