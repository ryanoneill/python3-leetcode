from triangle import Solution


def test_ex1():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution = Solution()
    result = solution.minimumTotal(triangle)
    assert result == 11


def test_ex2():
    triangle = [[-10]]
    solution = Solution()
    result = solution.minimumTotal(triangle)
    assert result == -10
