from tree_node import TreeNode
from typing import List, Optional


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        index_pre = 0
        index_post = 0

        def worker() -> Optional[TreeNode]:
            nonlocal index_pre
            nonlocal index_post

            value = preorder[index_pre]
            node = TreeNode(int(value))

            index_pre += 1

            if value != postorder[index_post]:
                node.left = worker()

            if value != postorder[index_post]:
                node.right = worker()

            index_post += 1

            return node

        return worker()
