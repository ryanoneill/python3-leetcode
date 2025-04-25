from pascals_triangle import Solution


def test_ex1():
    numRows = 5
    solution = Solution()
    result = solution.generate(numRows)
    assert result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_ex2():
    numRows = 1
    solution = Solution()
    result = solution.generate(numRows)
    assert result == [[1]]
