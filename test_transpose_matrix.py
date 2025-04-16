from transpose_matrix import Solution

def test_ex1():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    result = solution.transpose(matrix)
    assert result == [[1,4,7],[2,5,8],[3,6,9]]

def test_ex2():
    matrix = [[1,2,3],[4,5,6]]
    solution = Solution()
    result = solution.transpose(matrix)
    assert result == [[1,4],[2,5],[3,6]]
