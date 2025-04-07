from tree_node import TreeNode
from collections import deque
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = 0
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(0, n):
                item = queue.popleft()
                if i == 0:
                    result = item.val
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)

        return result
