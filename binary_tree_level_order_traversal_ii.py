from queue import deque
from tree_node import TreeNode
from typing import Optional, List


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        items = deque()
        if root:
            items.append(root)

        while items:
            n = len(items)
            level = []
            for _ in range(n):
                item = items.popleft()
                level.append(item.val)
                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)
            results.append(level)

        return list(reversed(results))
