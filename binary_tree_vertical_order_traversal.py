from tree_node import TreeNode
from typing import List, Optional

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cache = {}
        def worker(node: Optional[TreeNode], x: int, y: int) -> None:
            if node:
                if not x in cache:
                    cache[x] = {}
                column = cache[x]
                if y in column:
                    column[y].append(node.val)
                else:
                    column[y] = [node.val]

                worker(node.left, x-1, y+1)
                worker(node.right, x+1, y+1)

        worker(root, 0, 0)

        results = []
        for _, column in sorted(cache.items()):
            result = []
            for _, values in sorted(column.items()):
                for value in values:
                    result.append(value)
            results.append(result)

        return results
