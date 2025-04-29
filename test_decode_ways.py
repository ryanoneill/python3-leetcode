from decode_ways import Solution

def test_ex1():
    s = "12"
    solution = Solution()
    result = solution.numDecodings(s)
    assert result == 2

def test_ex2():
    s = "226"
    solution = Solution()
    result = solution.numDecodings(s)
    assert result == 3

def test_ex3():
    s = "06"
    solution = Solution()
    result = solution.numDecodings(s)
    assert result == 0
