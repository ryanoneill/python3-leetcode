from as_far_from_land_as_possible import Solution

def test_ex1():
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    solution = Solution()
    result = solution.maxDistance(grid)
    assert result == 2

# def test_ex2():
#     grid = [[1,0,0],[0,0,0],[0,0,0]]
#     solution = Solution()
#     result = solution.maxDistance(grid)
#     assert result == 4
