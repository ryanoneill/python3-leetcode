from unique_paths_ii import Solution

def test_ex1():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    assert result == 2

def test_ex2():
    obstacleGrid = [[0,1],[0,0]]
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    assert result == 1
