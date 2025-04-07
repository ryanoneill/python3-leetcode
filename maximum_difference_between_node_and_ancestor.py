from tree_node import TreeNode
from typing import Optional


class Solution:
    def __worker(self, node: Optional[TreeNode], minimum: int, maximum: int) -> int:
        value = node.val
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        result = abs(maximum - minimum)
        if node.left:
            left_result = self.__worker(node.left, minimum, maximum)
            result = max(result, left_result)
        if node.right:
            right_result = self.__worker(node.right, minimum, maximum)
            result = max(result, right_result)
        return result

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.__worker(root, root.val, root.val)
