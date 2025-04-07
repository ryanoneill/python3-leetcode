from tree_node import TreeNode
from typing import List, Optional


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = {}

        def worker(node: Optional[TreeNode], row: int, col: int) -> None:
            if node:
                value = node.val
                if col not in cols:
                    cols[col] = {}
                rows = cols[col]
                if row not in rows:
                    rows[row] = [value]
                else:
                    rows[row].append(value)
                worker(node.left, row + 1, col - 1)
                worker(node.right, row + 1, col + 1)

        worker(root, 0, 0)

        results = []
        for key in sorted(cols):
            result = []
            rows = cols[key]
            for key in sorted(rows):
                data = rows[key]
                for value in sorted(data):
                    result.append(value)
            results.append(result)

        return results
