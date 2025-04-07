from count_the_number_of_complete_components import Solution


def test_ex1():
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    solution = Solution()
    result = solution.countCompleteComponents(n, edges)
    assert result == 3


def test_ex2():
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    solution = Solution()
    result = solution.countCompleteComponents(n, edges)
    assert result == 1
