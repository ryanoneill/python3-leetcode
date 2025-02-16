from toeplitz_matrix import Solution

def test_ex1():
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    solution = Solution()
    result = solution.isToeplitzMatrix(matrix)
    assert result

def test_ex2():
    matrix = [[1,2],[2,2]]
    solution = Solution()
    result = solution.isToeplitzMatrix(matrix)
    assert not result
