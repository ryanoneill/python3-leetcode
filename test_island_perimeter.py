from island_perimeter import Solution


def test_ex1():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    solution = Solution()
    result = solution.islandPerimeter(grid)
    assert result == 16


def test_ex2():
    grid = [[1]]
    solution = Solution()
    result = solution.islandPerimeter(grid)
    assert result == 4
