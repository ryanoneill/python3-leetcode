from closest_prime_numbers_in_range import Solution

def test_ex1():
    left = 10
    right = 19
    solution = Solution()
    result = solution.closestPrimes(left, right)
    assert result == [11,13]

def test_ex2():
    left = 4
    right = 6
    solution = Solution()
    result = solution.closestPrimes(left, right)
    assert result == [-1,-1]

def test_ex3():
    left = 19
    right = 31
    solution = Solution()
    result = solution.closestPrimes(left, right)
    assert result == [29,31]

def test_ex4():
    left = 1
    right = 1000000
    solution = Solution()
    result = solution.closestPrimes(left, right)
    assert result == [2,3]

def test_ex5():
    left = 710119
    right = 710189
    solution = Solution()
    result = solution.closestPrimes(left, right)
    assert result == [710119, 710189]
