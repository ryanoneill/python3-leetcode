from count_odd_numbers_in_an_interval_range import Solution

def test_ex1():
    low = 3
    high = 7
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 3

def test_ex2():
    low = 8
    high = 10
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 1

def test_ex3():
    low = 7
    high = 10
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 2

def test_ex4():
    low = 8
    high = 9
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 1

def test_ex5():
    low = 8
    high = 8
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 0

def test_ex6():
    low = 9
    high = 9
    solution = Solution()
    result = solution.countOdds(low, high)
    assert result == 1
