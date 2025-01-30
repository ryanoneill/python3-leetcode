from queue import deque
from tree_node import TreeNode
from typing import Optional

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = 0
        items = deque()
        if root:
            items.append(root)

        while items:
            n = len(items)
            level_sum = 0
            for _ in range(n):
                item = items.popleft()
                level_sum += item.val
                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)
            result = level_sum

        return result
