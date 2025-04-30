from minimum_path_sum import Solution

def test_ex1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    solution = Solution()
    result = solution.minPathSum(grid)
    assert result == 7

def test_ex2():
    grid = [[1,2,3],[4,5,6]]
    solution = Solution()
    result = solution.minPathSum(grid)
    assert result == 12
