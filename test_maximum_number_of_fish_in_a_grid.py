from maximum_number_of_fish_in_a_grid import Solution

def test_ex1():
    grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    solution = Solution()
    result = solution.findMaxFish(grid)
    assert result == 7

def test_ex2():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    solution = Solution()
    result = solution.findMaxFish(grid)
    assert result == 1
