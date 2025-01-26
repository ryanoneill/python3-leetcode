from tree_node import TreeNode
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        if root:
            result = 1
            if root.left and root.right:
                left = self.minDepth(root.left)
                right = self.minDepth(root.right)
                result += min(left, right)
            elif root.left:
                result += self.minDepth(root.left)
            elif root.right:
                result += self.minDepth(root.right)

        return result
