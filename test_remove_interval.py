from remove_interval import Solution


def test_ex1():
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    solution = Solution()
    results = solution.removeInterval(intervals, toBeRemoved)
    assert results == [[0, 1], [6, 7]]


def test_ex2():
    intervals = [[0, 5]]
    toBeRemoved = [2, 3]
    solution = Solution()
    results = solution.removeInterval(intervals, toBeRemoved)
    assert results == [[0, 2], [3, 5]]


def test_ex3():
    intervals = [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]]
    toBeRemoved = [-1, 4]
    solution = Solution()
    results = solution.removeInterval(intervals, toBeRemoved)
    assert results == [[-5, -4], [-3, -2], [4, 5], [8, 9]]
