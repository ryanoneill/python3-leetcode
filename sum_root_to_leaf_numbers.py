from tree_node import TreeNode
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(path: str, node: TreeNode) -> int:
            combined = path + str(node.val)
            if node.left and node.right:
                left = dfs(combined, node.left)
                right = dfs(combined, node.right)
                result = left + right
            elif node.left:
                result = dfs(combined, node.left)
            elif node.right:
                result = dfs(combined, node.right)
            else:
                result = int(combined)

            return result

        result = 0
        if root:
            result = dfs("", root)
        return result
