from tree_node import TreeNode
from typing import Optional

class Solution:
    def __worker(self, node: Optional[TreeNode], target: float, closest: int) -> int:
        result = closest
        if node:
            value = float(node.val)

            close_diff = abs(float(closest) - target)
            curr_diff = abs(value - target)

            if curr_diff == close_diff:
                result = min(closest, node.val)
            elif curr_diff < close_diff:
                result = node.val

            if target < value:
                result = self.__worker(node.left, target, result)
            else:
                result = self.__worker(node.right, target, result)

        return result

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = -1
        if root:
            result = self.__worker(root, target, root.val)
        return result
