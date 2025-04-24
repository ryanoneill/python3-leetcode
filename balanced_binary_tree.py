from tree_node import TreeNode
from typing import Optional, Tuple

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def worker(node: Optional[TreeNode]) -> Tuple[int, bool]:
            result = (0, True)
            if node:
                left_height, left_balanced = worker(node.left)
                right_height, right_balanced = worker(node.right)
                height = max(left_height, right_height) + 1
                if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
                    result = (height, True)
                else:
                    result = (height, False)

            return result

        _, result = worker(root)

        return result
