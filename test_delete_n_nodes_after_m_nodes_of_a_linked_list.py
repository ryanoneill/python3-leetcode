from list_node import from_list, to_list
from delete_n_nodes_after_m_nodes_of_a_linked_list import Solution

def test_ex1():
    items = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    m = 2
    n = 3
    head = from_list(items)
    solution = Solution()
    result = solution.deleteNodes(head, m, n)
    assert to_list(result) == [1,2,6,7,11,12]

def test_ex2():
    items = [1,2,3,4,5,6,7,8,9,10,11]
    m = 1
    n = 3
    head = from_list(items)
    solution = Solution()
    result = solution.deleteNodes(head, m, n)
    assert to_list(result) == [1,5,9]
