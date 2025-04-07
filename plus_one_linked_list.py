from list_node import ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        result = head
        stack = []

        current = head
        while current:
            stack.append(current)
            current = current.next
        carry = True
        while carry:
            if stack:
                item = stack.pop()
                if item.val == 9:
                    item.val = 0
                else:
                    item.val += 1
                    carry = False
            else:
                result = ListNode(1, head)
                carry = False

        return result
