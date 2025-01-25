from list_node import from_list, to_list
from middle_of_the_linked_list import Solution

def test_ex1():
    items = [1,2,3,4,5]
    head = from_list(items)
    solution = Solution()
    result = solution.middleNode(head)
    assert to_list(result) == [3,4,5]

def test_ex2():
    items = [1,2,3,4,5,6]
    head = from_list(items)
    solution = Solution()
    result = solution.middleNode(head)
    assert to_list(result) == [4,5,6]
