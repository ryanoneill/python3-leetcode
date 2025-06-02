from heapq import heappush, heappop
from list_node import ListNode
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        current = None

        heap = []

        for i, node in enumerate(lists):
            if node:
                tail = node.next
                lists[i] = tail
                node.next = None
                item = (node.val, i, node)
                heappush(heap, item)

        while heap:
            _, i, node = heappop(heap)
            if not result:
                result = node
                current = result
            elif current:
                current.next = node
                current = current.next

            next_node = lists[i]
            if next_node:
                tail = next_node.next
                lists[i] = tail
                next_node.next = None
                item = (next_node.val, i, next_node)
                heappush(heap, item)

        return result
