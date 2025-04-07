from list_node import ListNode
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        return slow
