from list_node import from_list, to_list
from merge_k_sorted_lists import Solution

def test_ex1():
    lists = [[1,4,5], [1,3,4], [2,6]]
    lists = list(map(from_list, lists))
    solution = Solution()
    result = solution.mergeKLists(lists)
    assert to_list(result) == [1,1,2,3,4,4,5,6]

def test_ex2():
    lists = []
    lists = list(map(from_list, lists))
    solution = Solution()
    result = solution.mergeKLists(lists)
    assert to_list(result) == []

def test_ex3():
    lists = [[]]
    lists = list(map(from_list, lists))
    solution = Solution()
    result = solution.mergeKLists(lists)
    assert to_list(result) == []
