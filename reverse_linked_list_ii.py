from list_node import ListNode
from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        fake = ListNode(0)
        fake.next = head

        previous = fake
        current = fake.next

        for _ in range(1, left):
            previous = current
            current = current.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = previous.next
            previous.next = temp

        return fake.next
