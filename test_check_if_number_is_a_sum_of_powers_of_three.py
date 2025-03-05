from check_if_number_is_a_sum_of_powers_of_three import Solution

def test_ex1():
    n = 12
    solution = Solution()
    result = solution.checkPowersOfThree(n)
    assert result

def test_ex2():
    n = 91
    solution = Solution()
    result = solution.checkPowersOfThree(n)
    assert result

def test_ex3():
    n = 21
    solution = Solution()
    result = solution.checkPowersOfThree(n)
    assert not result
