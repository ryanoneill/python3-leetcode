from find_the_count_of_good_integers import Solution

def test_ex1():
    n = 3
    k = 5
    solution = Solution()
    result = solution.countGoodIntegers(n, k)
    assert result == 27

def test_ex2():
    n = 1
    k = 4
    solution = Solution()
    result = solution.countGoodIntegers(n, k)
    assert result == 2

def test_ex3():
    n = 5
    k = 6
    solution = Solution()
    result = solution.countGoodIntegers(n, k)
    assert result == 2468

def test_ex4():
    n = 10
    k = 9
    solution = Solution()
    result = solution.countGoodIntegers(n, k)
    assert result == 4610368
