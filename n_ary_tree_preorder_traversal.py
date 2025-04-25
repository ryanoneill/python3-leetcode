from node import Node
from typing import List, Optional


class Solution:
    def preorder(self, root: Optional["Node"]) -> List[int]:
        results = []

        def worker(node: Optional["Node"]):
            if node:
                results.append(node.val)
                for child in node.children:
                    worker(child)

        worker(root)

        return results
