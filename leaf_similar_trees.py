from tree_node import TreeNode
from itertools import zip_longest
from typing import Iterator, Optional


class Solution:
    def leaf_gen(self, root: Optional[TreeNode]) -> Iterator[int]:
        def worker(node: Optional[TreeNode]):
            if node:
                leaf = node.left is None and node.right is None
                if leaf:
                    yield node.val
                else:
                    if node.left:
                        yield from worker(node.left)
                    if node.right:
                        yield from worker(node.right)

        yield from worker(root)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = True
        gen1 = self.leaf_gen(root1)
        gen2 = self.leaf_gen(root2)
        for val1, val2 in zip_longest(gen1, gen2):
            if val1 is None or val2 is None or val1 != val2:
                result = False
                break

        return result
