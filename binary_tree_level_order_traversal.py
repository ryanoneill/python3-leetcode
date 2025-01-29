from tree_node import TreeNode
from typing import List, Optional
from queue import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        values = deque()
        if root:
            values.append(root)

        while values:
            n = len(values)
            level = []
            for _ in range(n):
                value = values.popleft()
                level.append(value.val)
                if value.left:
                    values.append(value.left)
                if value.right:
                    values.append(value.right)
            result.append(level)

        return result


