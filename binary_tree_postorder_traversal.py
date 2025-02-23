from tree_node import TreeNode
from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def worker(results: List[int], node: Optional[TreeNode]):
            if node:
                worker(results, node.left)
                worker(results, node.right)
                results.append(int(node.val))

        results = []
        worker(results, root)
        return results
