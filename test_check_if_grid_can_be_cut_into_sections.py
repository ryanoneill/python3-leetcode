from check_if_grid_can_be_cut_into_sections import Solution


def test_ex1():
    n = 5
    rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
    solution = Solution()
    result = solution.checkValidCuts(n, rectangles)
    assert result


def test_ex2():
    n = 4
    rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
    solution = Solution()
    result = solution.checkValidCuts(n, rectangles)
    assert result


def test_ex3():
    n = 4
    rectangles = [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]
    solution = Solution()
    result = solution.checkValidCuts(n, rectangles)
    assert not result
