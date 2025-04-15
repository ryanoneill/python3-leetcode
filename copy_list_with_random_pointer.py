from random_node import Node
from typing import Optional

class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        map = {}

        def worker(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return None
            elif node in map:
                return map[node]
            else:
                result = Node(node.val)
                map[node] = result
                result.next = worker(node.next)
                result.random = worker(node.random)
                return result

        return worker(head)
