from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    next = head
    while next is not None:
        result.append(next.val)
        next = next.next
    return result

def from_list(items: List[int]) -> Optional[ListNode]:
    head = None
    previous = None
    for value in items:
        current = ListNode(value)
        if previous is None:
            previous = current
            head = current
        else:
            previous.next = current
            previous = current
    return head


