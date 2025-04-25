from count_ways_to_build_good_strings import Solution


def test_ex1():
    low = 3
    high = 3
    zero = 1
    one = 1
    solution = Solution()
    result = solution.countGoodStrings(low, high, zero, one)
    assert result == 8


def test_ex2():
    low = 2
    high = 3
    zero = 1
    one = 2
    solution = Solution()
    result = solution.countGoodStrings(low, high, zero, one)
    assert result == 5
