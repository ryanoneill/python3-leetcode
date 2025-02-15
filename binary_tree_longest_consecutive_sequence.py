from tree_node import TreeNode
from typing import Optional

class Solution:
    def worker(self, root: Optional[TreeNode], parent: int, count: int) -> int:
        result = count
        if root:
            value = root.val
            if value == parent + 1:
                count += 1
            else:
                count = 1
            left = self.worker(root.left, value, count)
            right = self.worker(root.right, value, count)
            result = max(result, left, right)
        return result

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root:
            left = self.worker(root.left, root.val, 1)
            right = self.worker(root.right, root.val, 1)
            result = max(left, right)

        return result

