from tree_node import TreeNode
from typing import Optional


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def worker(node: Optional[TreeNode]) -> Optional[TreeNode]:
            result = node
            if node:
                left = worker(node.left)
                right = worker(node.right)
                if left or right:
                    node.left = left
                    node.right = right
                    result = node
                elif node.val == target:
                    result = None
                else:
                    node.left = None
                    node.right = None
                    result = node
            return result

        return worker(root)
