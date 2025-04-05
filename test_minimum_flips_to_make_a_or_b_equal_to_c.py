from minimum_flips_to_make_a_or_b_equal_to_c import Solution

def test_ex1():
    a = 2
    b = 6
    c = 5
    solution = Solution()
    result = solution.minFlips(a, b, c)
    assert result == 3

def test_ex2():
    a = 4
    b = 2
    c = 7
    solution = Solution()
    result = solution.minFlips(a, b, c)
    assert result == 1

def test_ex3():
    a = 1
    b = 2
    c = 3
    solution = Solution()
    result = solution.minFlips(a, b, c)
    assert result == 0

def test_ex4():
    a = 6
    b = 12
    c = 10
    solution = Solution()
    result = solution.minFlips(a, b, c)
    assert result == 2
