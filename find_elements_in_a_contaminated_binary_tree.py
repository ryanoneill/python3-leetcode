from queue import deque
from tree_node import TreeNode
from typing import Optional, Set

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        nodes = deque()
        nodes.append((root, 0))

        while nodes:
            n = len(nodes)
            for _ in range(n):
                (node, value) = nodes.popleft()
                if node:
                    self.values.add(value)
                    left = value * 2 + 1
                    nodes.append((node.left, left))
                    right = value * 2 + 2
                    nodes.append((node.right, right))

    def find(self, target: int) -> bool:
        return target in self.values
