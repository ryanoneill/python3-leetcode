from list_node import from_list, to_list
from remove_duplicates_from_sorted_list import Solution

def test_ex1():
    items = [1,1,2]
    head = from_list(items)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    assert to_list(result) == [1,2]

def test_ex2():
    items = [1,1,2,3,3]
    head = from_list(items)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    assert to_list(result) == [1,2,3]
