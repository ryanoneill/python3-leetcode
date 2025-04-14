from node import Node
from typing import List

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = 0
        for node in tree:
            total += node.val or 0
            for child in node.children:
                if child:
                    total -= child.val or 0

        result = tree[0]
        for node in tree:
            if node.val == total:
                result = node
                break

        return result
