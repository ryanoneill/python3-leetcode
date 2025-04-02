from maximum_odd_binary_value import Solution

def test_ex1():
    s = "010"
    solution = Solution()
    result = solution.maximumOddBinaryNumber(s)
    assert result == "001"

def test_ex2():
    s = "0101"
    solution = Solution()
    result = solution.maximumOddBinaryNumber(s)
    assert result == "1001"
