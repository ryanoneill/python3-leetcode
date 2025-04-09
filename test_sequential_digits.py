from sequential_digits import Solution

def test_ex1():
    low = 100
    high = 300
    solution = Solution()
    result = solution.sequentialDigits(low, high)
    assert result == [123, 234]

def test_ex2():
    low = 1000
    high = 13000
    solution = Solution()
    result = solution.sequentialDigits(low, high)
    assert result == [1234, 2345, 3456, 4567, 5678, 6789,12345]
