from list_node import from_list, to_list
from plus_one_linked_list import Solution


def test_ex1():
    items = [1, 2, 3]
    head = from_list(items)
    solution = Solution()
    result = solution.plusOne(head)
    assert to_list(result) == [1, 2, 4]


def test_ex2():
    items = [0]
    head = from_list(items)
    solution = Solution()
    result = solution.plusOne(head)
    assert to_list(result) == [1]


def test_ex3():
    items = [9]
    head = from_list(items)
    solution = Solution()
    result = solution.plusOne(head)
    assert to_list(result) == [1, 0]
