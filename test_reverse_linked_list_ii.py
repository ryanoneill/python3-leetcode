from list_node import from_list, to_list
from reverse_linked_list_ii import Solution

def test_ex1():
    items = [1,2,3,4,5]
    head = from_list(items)
    left = 2
    right = 4
    solution = Solution()
    result = solution.reverseBetween(head, left, right)
    assert to_list(result) == [1,4,3,2,5]

def test_ex2():
    items = [5]
    head = from_list(items)
    left = 1
    right = 1
    solution = Solution()
    result = solution.reverseBetween(head, left, right)
    assert to_list(result) == [5]
