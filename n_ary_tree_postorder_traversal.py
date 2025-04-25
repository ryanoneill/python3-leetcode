from node import Node
from typing import List, Optional


class Solution:
    def postorder(self, root: Optional["Node"]) -> List[int]:
        results = []

        def worker(node: Optional["Node"]):
            if node:
                if node.children:
                    for child in node.children:
                        worker(child)

                results.append(node.val)

        worker(root)

        return results
