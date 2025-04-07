from minimum_operations_to_make_a_uni_value_grid import Solution


def test_ex1():
    grid = [[2, 4], [6, 8]]
    x = 2
    solution = Solution()
    result = solution.minOperations(grid, x)
    assert result == 4


def test_ex2():
    grid = [[1, 5], [2, 3]]
    x = 1
    solution = Solution()
    result = solution.minOperations(grid, x)
    assert result == 5


def test_ex3():
    grid = [[1, 2], [3, 4]]
    x = 2
    solution = Solution()
    result = solution.minOperations(grid, x)
    assert result == -1
