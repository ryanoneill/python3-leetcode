from count_symmetric_integers import Solution

def test_ex1():
    low = 1
    high = 100
    solution = Solution()
    result = solution.countSymmetricIntegers(low, high)
    assert result == 9

def test_ex2():
    low = 1200
    high = 1230
    solution = Solution()
    result = solution.countSymmetricIntegers(low, high)
    assert result == 4
