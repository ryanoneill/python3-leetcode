from list_node import ListNode
from typing import Optional


class Solution:
    def deleteNodes(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        result = head
        previous = head
        current = head

        done = False
        while not done:
            for _ in range(m):
                previous = current
                current = current.next
                if current is None:
                    done = True
                    break
            if not done:
                for _ in range(n):
                    current = current.next
                    previous.next = current
                    if current is None:
                        done = True
                        break

        return result
