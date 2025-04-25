from node import Node
from typing import Optional


class Solution:
    def maxDepth(self, root: "Node") -> int:
        def worker(node: Optional["Node"], level: int) -> int:
            result = level
            if node:
                level += 1
                result = level
                for child in node.children:
                    result = max(result, worker(child, level))
            return result

        return worker(root, 0)
