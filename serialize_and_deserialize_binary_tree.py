from queue import deque
from tree_node import TreeNode
from typing import Optional

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        items = deque()
        items.append(root)

        while items:
            n = len(items)
            for _ in range(n):
                item = items.popleft()
                if item:
                    result.append(str(item.val))
                    items.append(item.left)
                    items.append(item.right)
                else:
                    result.append("null")

        while result and result[-1] == "null":
            result.pop()

        return "[" + ",".join(result) + "]"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            result = None
        else:
            result = None
            queue = deque()
            items = data[1:-1].split(",")
            n = len(items)
            i = 0

            while i < n:
                parent = None
                if queue:
                    parent = queue.popleft()
                if parent:
                    left = items[i]
                    if left != "null":
                        parent.left = TreeNode(int(left))
                        queue.append(parent.left)
                    i += 1
                    if i < n:
                        right = items[i]
                        i += 1
                        if right != "null":
                            parent.right = TreeNode(int(right))
                            queue.append(parent.right)
                else:
                    root = TreeNode(int(items[i]))
                    i += 1
                    result = root
                    queue.append(root)

        return result
