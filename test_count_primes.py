from count_primes import Solution

def test_ex1():
    n = 10
    solution = Solution()
    result = solution.countPrimes(n)
    assert result == 4

def test_ex2():
    n = 0
    solution = Solution()
    result = solution.countPrimes(n)
    assert result == 0

def test_ex3():
    n = 1
    solution = Solution()
    result = solution.countPrimes(n)
    assert result == 0

def test_ex4():
    n = 2
    solution = Solution()
    result = solution.countPrimes(n)
    assert result == 0

def test_ex5():
    n = 5000000
    solution = Solution()
    result = solution.countPrimes(n)
    assert result == 348513
