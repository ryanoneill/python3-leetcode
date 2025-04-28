from shift_2d_grid import Solution

def test_ex1():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    solution = Solution()
    result = solution.shiftGrid(grid, k)
    assert result == [[9,1,2],[3,4,5],[6,7,8]]

def test_ex2():
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    solution = Solution()
    result = solution.shiftGrid(grid, k)
    assert result == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

def test_ex3():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 9
    solution = Solution()
    result = solution.shiftGrid(grid, k)
    assert result == [[1,2,3],[4,5,6],[7,8,9]]
