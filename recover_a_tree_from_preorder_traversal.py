from tree_node import TreeNode
from typing import Optional


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        values = traversal.split("-")
        result = TreeNode(int(values[0]))
        nodes = [result]

        i = 1
        n = len(values)
        while i < n:
            level = 1
            value = values[i]
            while not value.isnumeric():
                level += 1
                i += 1
                value = values[i]
            while len(nodes) > level:
                nodes.pop()
            parent = nodes[-1]
            node = TreeNode(int(value))
            nodes.append(node)
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            i += 1

        return result
