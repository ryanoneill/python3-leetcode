from hamming_distance import Solution

def test_ex1():
    x = 1
    y = 4
    solution = Solution()
    result = solution.hammingDistance(x, y)
    assert result == 2

def test_ex2():
    x = 3
    y = 1
    solution = Solution()
    result = solution.hammingDistance(x, y)
    assert result == 1
