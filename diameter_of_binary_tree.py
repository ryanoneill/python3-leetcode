from tree_node import TreeNode
from typing import Optional


class Solution:
    def __worker(self, node: Optional[TreeNode], diameter: int) -> (int, int):
        result_diam = 0
        result_depth = 0

        if node:
            (left_depth, left_diam) = self.__worker(node.left, diameter)
            (right_depth, right_diam) = self.__worker(node.right, diameter)

            result_diam = max(diameter, left_diam, right_diam, left_depth + right_depth)
            result_depth = max(left_depth, right_depth) + 1

        return result_depth, result_diam

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        (_, result) = self.__worker(root, 0)
        return result
