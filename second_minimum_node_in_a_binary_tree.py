from tree_node import TreeNode
from typing import Optional


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def worker(node: Optional[TreeNode], first: int) -> int:
            result = -1
            if node:
                value = node.val
                if value == first:
                    left_result = worker(node.left, first)
                    right_result = worker(node.right, first)
                    if left_result != -1 and right_result != -1:
                        result = min(left_result, right_result)
                    elif left_result != -1:
                        result = left_result
                    elif right_result != -1:
                        result = right_result
                else:
                    result = value
            return result

        result = -1
        if root:
            result = worker(root, root.val)
        return result
