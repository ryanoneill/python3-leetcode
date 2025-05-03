from minimum_domino_rotations_for_equal_row import Solution

def test_ex1():
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]
    solution = Solution()
    result = solution.minDominoRotations(tops, bottoms)
    assert result == 2

def test_ex2():
    tops = [3,5,1,2,3]
    bottoms = [3,6,3,3,4]
    solution = Solution()
    result = solution.minDominoRotations(tops, bottoms)
    assert result == -1
