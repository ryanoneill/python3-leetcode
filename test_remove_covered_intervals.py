from remove_covered_intervals import Solution

def test_ex1():
    intervals = [[1,4],[3,6],[2,8]]
    solution = Solution()
    result = solution.removeCoveredIntervals(intervals)
    assert result == 2

def test_ex2():
    intervals = [[1,4],[2,3]]
    solution = Solution()
    result = solution.removeCoveredIntervals(intervals)
    assert result == 1

def test_ex3():
    intervals = [[1,2],[1,4],[2,3]]
    solution = Solution()
    result = solution.removeCoveredIntervals(intervals)
    assert result == 1
