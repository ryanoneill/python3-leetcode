from number_of_one_bits import Solution

def test_ex1():
    n = 11
    solution = Solution()
    result = solution.hammingWeight(n)
    assert result == 3

def test_ex2():
    n = 128
    solution = Solution()
    result = solution.hammingWeight(n)
    assert result == 1

def test_ex3():
    n = 2147483645
    solution = Solution()
    result = solution.hammingWeight(n)
    assert result == 30
