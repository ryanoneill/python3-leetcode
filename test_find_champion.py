from find_champion import Solution

def test_ex1():
    grid = [[0,1],[0,0]]
    solution = Solution()
    result = solution.findChampion(grid)
    assert result == 0

def test_ex2():
    grid = [[0,0,1],[1,0,1],[0,0,0]]
    solution = Solution()
    result = solution.findChampion(grid)
    assert result == 1
