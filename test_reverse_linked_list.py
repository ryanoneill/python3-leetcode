from list_node import from_list, to_list
from reverse_linked_list import Solution

def test_ex1():
    items = [1,2,3,4,5]
    head = from_list(items)
    solution = Solution()
    result = solution.reverseList(head)
    assert to_list(result) == [5,4,3,2,1]

def test_ex2():
    items = [1,2]
    head = from_list(items)
    solution = Solution()
    result = solution.reverseList(head)
    assert to_list(result) == [2,1]

def test_ex3():
    items = []
    head = from_list(items)
    solution = Solution()
    result = solution.reverseList(head)
    assert to_list(result) == []

def test_ex4():
    items = [1]
    head = from_list(items)
    solution = Solution()
    result = solution.reverseList(head)
    assert to_list(result) == [1]

