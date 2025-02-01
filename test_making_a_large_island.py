from making_a_large_island import Solution

def test_ex1():
    grid = [[1,0],[0,1]]
    solution = Solution()
    result = solution.largestIsland(grid)
    assert result == 3

def test_ex2():
    grid = [[1,1],[1,0]]
    solution = Solution()
    result = solution.largestIsland(grid)
    assert result == 4

def test_ex3():
    grid = [[1,1],[1,1]]
    solution = Solution()
    result = solution.largestIsland(grid)
    assert result == 4

def test_ex4():
    grid = [[0,0],[0,0]]
    solution = Solution()
    result = solution.largestIsland(grid)
    assert result == 1

def test_ex5():
    grid = [[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]
    solution = Solution()
    result = solution.largestIsland(grid)
    for row in grid:
        print(row)
    assert result == 18
