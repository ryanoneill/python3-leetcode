from node import Node
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        results = []

        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                item = queue.popleft()
                if item:
                    level.append(item.val)
                    for child in item.children:
                        queue.append(child)

            if level:
                results.append(level)

        return results
