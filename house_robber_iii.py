from tree_node import TreeNode

from typing import Optional


# TODO: Improve Runtime
class Solution:
    def worker(
        self, cache: dict, node: Optional[TreeNode], skip: bool, num: int
    ) -> int:
        key = (num, skip)
        result = 0
        if key in cache:
            result = cache[key]
        else:
            if node:
                result = self.worker(cache, node.left, False, num * 2) + self.worker(
                    cache, node.right, False, num * 2 + 1
                )
                if not skip:
                    candidate = (
                        node.val
                        + self.worker(cache, node.left, True, num * 2)
                        + self.worker(cache, node.right, True, num * 2 + 1)
                    )
                    result = max(result, candidate)
            cache[key] = result

        return result

    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        yes = self.worker(cache, root, True, 1)
        no = self.worker(cache, root, False, 1)
        result = max(yes, no)

        return result
