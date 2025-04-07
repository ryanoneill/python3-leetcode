from tree_node import TreeNode
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def worker(results: List[int], node: Optional[TreeNode]):
            if node:
                results.append(int(node.val))
                worker(results, node.left)
                worker(results, node.right)

        results = []
        worker(results, root)
        return results
