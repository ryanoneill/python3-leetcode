from tree_node import TreeNode
from typing import Optional


class State:
    def __init__(self, values: int = 0, nodes: int = 0, avg: float = 0.0):
        self.values = values
        self.nodes = nodes
        self.avg = avg


class Solution:
    def valueState(self, root: Optional[TreeNode]) -> State:
        result = State()
        if root is not None:
            left = self.valueState(root.left)
            right = self.valueState(root.right)

            result.values = left.values + right.values + root.val
            result.nodes = left.nodes + right.nodes + 1
            average = result.values / result.nodes
            result.avg = max(average, left.avg, right.avg)

        return result

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        state = self.valueState(root)
        return state.avg
