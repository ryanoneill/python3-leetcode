from count_days_without_meetings import Solution


def test_ex1():
    n = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 2


def test_ex2():
    n = 5
    meetings = [[2, 4], [1, 3]]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 1


def test_ex3():
    n = 6
    meetings = [[1, 6]]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 0


def test_ex4():
    n = 14
    meetings = [
        [6, 11],
        [7, 13],
        [8, 9],
        [5, 8],
        [3, 13],
        [11, 13],
        [1, 3],
        [5, 10],
        [8, 13],
        [3, 9],
    ]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 1


def test_ex5():
    n = 14
    meetings = [[2, 3], [3, 4], [12, 14], [8, 10]]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 5


def test_ex6():
    n = 50
    meetings = [
        [22, 31],
        [7, 42],
        [30, 46],
        [9, 33],
        [9, 18],
        [23, 39],
        [4, 8],
        [18, 19],
    ]
    solution = Solution()
    result = solution.countDays(n, meetings)
    assert result == 7
