from tree_node import TreeNode
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def worker(node: Optional[TreeNode]):
            nonlocal results
            if node:
                worker(node.left)
                results.append(node.val)
                worker(node.right)

        worker(root)
        return results
