from path_with_minimum_effort import Solution

def test_ex1():
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    solution = Solution()
    result = solution.minimumEffortPath(heights)
    assert result == 2

def test_ex2():
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    solution = Solution()
    result = solution.minimumEffortPath(heights)
    assert result == 1

def test_ex3():
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    solution = Solution()
    result = solution.minimumEffortPath(heights)
    assert result == 0
