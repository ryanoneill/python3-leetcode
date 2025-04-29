from number_of_closed_islands import Solution

def test_ex1():
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    solution = Solution()
    result = solution.closedIsland(grid)
    assert result == 2

def test_ex2():
    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    solution = Solution()
    result = solution.closedIsland(grid)
    assert result == 1

def test_ex3():
    grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
    solution = Solution()
    result = solution.closedIsland(grid)
    assert result == 2
