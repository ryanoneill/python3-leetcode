from list_node import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = None
        next = head

        while next is not None:
            current = next
            next = next.next
            current.next = previous
            previous = current

        return current
