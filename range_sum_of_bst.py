from tree_node import TreeNode
from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def worker(node: Optional[TreeNode]) -> int:
            result = 0
            if node:
                if low <= node.val <= high:
                    result += node.val
                if low < node.val:
                    result += worker(node.left)
                if high > node.val:
                    result += worker(node.right)

            return result
        return worker(root)
