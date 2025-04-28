from zigzag_conversion import Solution

def test_ex1():
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    assert result == "PAHNAPLSIIGYIR"

def test_ex2():
    s = "PAYPALISHIRING"
    numRows = 4
    solution = Solution()
    result = solution.convert(s, numRows)
    assert result == "PINALSIGYAHRPI"

def test_ex3():
    s = "A"
    numRows = 1
    solution = Solution()
    result = solution.convert(s, numRows)
    assert result == "A"

def test_ex4():
    s = "AB"
    numRows = 1
    solution = Solution()
    result = solution.convert(s, numRows)
    assert result == "AB"
