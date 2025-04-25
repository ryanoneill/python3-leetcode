from matrix_diagonal_sum import Solution


def test_ex1():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    result = solution.diagonalSum(mat)
    assert result == 25


def test_ex2():
    mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    solution = Solution()
    result = solution.diagonalSum(mat)
    assert result == 8


def test_ex3():
    mat = [[5]]
    solution = Solution()
    result = solution.diagonalSum(mat)
    assert result == 5
