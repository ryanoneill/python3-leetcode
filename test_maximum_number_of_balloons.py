from maximum_number_of_balloons import Solution

def test_ex1():
    text = "nlaebolko"
    solution = Solution()
    result = solution.maxNumberOfBalloons(text)
    assert result == 1

def test_ex2():
    text = "loonbalxballpoon"
    solution = Solution()
    result = solution.maxNumberOfBalloons(text)
    assert result == 2

def test_ex3():
    text = "leetcode"
    solution = Solution()
    result = solution.maxNumberOfBalloons(text)
    assert result == 0
