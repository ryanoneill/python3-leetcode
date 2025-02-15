from sparse_matrix_multiplication import Solution

def test_ex1():
    mat1 = [[1,0,0],[-1,0,3]]
    mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    solution = Solution()
    result = solution.multiply(mat1, mat2)
    assert result == [[7,0,0],[-7,0,3]]

def test_ex2():
    mat1 = [[0]]
    mat2 = [[0]]
    solution = Solution()
    result = solution.multiply(mat1, mat2)
    assert result == [[0]]
