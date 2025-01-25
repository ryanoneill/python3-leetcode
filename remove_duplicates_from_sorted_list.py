from list_node import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        previous = None
        value = 101 # outside the range of values

        while head is not None:
            if head.val != value:
                value = head.val
                if previous is None:
                    result = head
                    previous = head
                else:
                    previous.next = head
                    previous = previous.next

            head = head.next
            previous.next = None

        return result

