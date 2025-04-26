from widest_vertical_area_between_two_points_containing_no_points import Solution

def test_ex1():
    points = [[8,7],[9,9],[7,4],[9,7]]
    solution = Solution()
    result = solution.maxWidthOfVerticalArea(points)
    assert result == 1

def test_ex2():
     points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
     solution = Solution()
     result = solution.maxWidthOfVerticalArea(points)
     assert result == 3
