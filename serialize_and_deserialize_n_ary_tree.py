from node import Node
from collections import deque
from typing import Optional


class Codec:
    def serialize(self, root: Optional[Node]) -> str:
        result = []

        if root:
            items = deque()
            items.append(root)

            while items:
                n = len(items)
                for _ in range(n):
                    item = items.popleft()
                    if item:
                        result.append(str(item.val))
                        items.append(None)
                        for child in item.children:
                            items.append(child)
                    else:
                        result.append("null")

        while result and result[-1] == "null":
            result.pop()

        return "[" + ",".join(result) + "]"

    def deserialize(self, data: str) -> Optional[Node]:
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
                if not parent:
                    root = Node(int(items[i]))
                    i += 1
                    result = root
                    queue.append(root)
                else:
                    next = items[i]
                    assert next == "null"
                    i += 1
                    children = []
                    while i < n and items[i] != "null":
                        child = Node(int(items[i]))
                        i += 1
                        children.append(child)
                        queue.append(child)
                    parent.children = children

        return result
