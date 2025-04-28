from convert_1d_array_into_2d_array import Solution

def test_ex1():
    original = [1,2,3,4]
    m = 2
    n = 2
    solution = Solution()
    result = solution.construct2DArray(original, m, n)
    assert result == [[1,2],[3,4]]

def test_ex2():
    original = [1,2,3]
    m = 1
    n = 3
    solution = Solution()
    result = solution.construct2DArray(original, m, n)
    assert result == [[1,2,3]]

def test_ex3():
    original = [1,2]
    m = 1
    n = 1
    solution = Solution()
    result = solution.construct2DArray(original, m, n)
    assert result == []
