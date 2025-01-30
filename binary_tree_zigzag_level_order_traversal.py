from queue import deque
from tree_node import TreeNode
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        result = []
        items = deque()
        if root:
            items.append(root)

        while items:
            level += 1
            n = len(items)
            values = []

            for _ in range(n):
                item = items.popleft()
                values.append(item.val)

                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)

            if level % 2 == 0:
                values.reverse()

            result.append(values)

        return result
