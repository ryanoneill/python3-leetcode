from find_the_punishment_number_of_an_integer import Solution

def test_ex1():
    n = 10
    solution = Solution()
    result = solution.punishmentNumber(n)
    assert result == 182

def test_ex2():
    n = 37
    solution = Solution()
    result = solution.punishmentNumber(n)
    assert result == 1478

def test_ex3():
    n = 45
    solution = Solution()
    result = solution.punishmentNumber(n)
    assert result == 3503
