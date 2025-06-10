from maximum_difference_between_even_and_odd_frequency_i import Solution

def test_ex1():
    s = "aaaaabbc"
    solution = Solution()
    result = solution.maxDifference(s)
    assert result == 3

def test_ex2():
    s = "abcabcab"
    solution = Solution()
    result = solution.maxDifference(s)
    assert result == 1

def test_ex3():
    s = "tzt"
    solution = Solution()
    result = solution.maxDifference(s)
    assert result == -1
