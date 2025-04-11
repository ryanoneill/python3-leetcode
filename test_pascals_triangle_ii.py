from pascals_triangle_ii import Solution

def test_ex1():
    rowIndex = 3
    solution = Solution()
    result = solution.getRow(rowIndex)
    assert result == [1,3,3,1]

def test_ex2():
    rowIndex = 0
    solution = Solution()
    result = solution.getRow(rowIndex)
    assert result == [1]

def test_ex3():
    rowIndex = 1
    solution = Solution()
    result = solution.getRow(rowIndex)
    assert result == [1,1]

def test_ex4():
    rowIndex = 4
    solution = Solution()
    result = solution.getRow(rowIndex)
    assert result == [1,4,6,4,1]
