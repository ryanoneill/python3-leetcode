from tree_node import TreeNode
from typing import Optional

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def worker(node: Optional[TreeNode]) -> bool:
            result = True
            if node:
                value = node.val
                if value == 0:
                    result = False
                elif value == 1:
                    result = True
                elif value == 2:
                    result = worker(node.left) or worker(node.right)
                elif value == 3:
                    result = worker(node.left) and worker(node.right)

            return result

        return worker(root)
