from search_a_2d_matrix import Solution

def test_ex1():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    assert result

def test_ex2():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    assert not result
