from number_of_islands import Solution

def test_ex1():
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    ]
    solution = Solution()
    result = solution.numIslands(grid)
    assert result == 1

def test_ex2():
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    ]
    solution = Solution()
    result = solution.numIslands(grid)
    assert result == 3


