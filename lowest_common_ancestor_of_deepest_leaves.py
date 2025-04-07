from tree_node import TreeNode
from typing import Optional, Tuple


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            result = (0, None)
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if left[0] > right[0]:
                    result = (left[0] + 1, left[1])
                elif left[0] < right[0]:
                    result = (right[0] + 1, right[1])
                else:
                    result = (left[0] + 1, node)

            return result

        result = dfs(root)[1]
        return result
