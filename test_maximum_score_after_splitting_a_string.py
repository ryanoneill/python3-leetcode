from maximum_score_after_splitting_a_string import Solution

def test_ex1():
    s = "011101"
    solution = Solution()
    result = solution.maxScore(s)
    assert result == 5

def test_ex2():
    s = "00111"
    solution = Solution()
    result = solution.maxScore(s)
    assert result == 5

def test_ex3():
    s = "1111"
    solution = Solution()
    result = solution.maxScore(s)
    assert result == 3
