from put_marbles_in_a_bag import Solution

def test_ex1():
    weights = [1,3,5,1]
    k = 2
    solution = Solution()
    result = solution.putMarbles(weights, k)
    assert result == 4

def test_ex2():
    weights = [1, 3]
    k = 2
    solution = Solution()
    result = solution.putMarbles(weights, k)
    assert result == 0

def test_ex3():
    weights = [25,74,16,51,12,48,15,5]
    k = 1
    solution = Solution()
    result = solution.putMarbles(weights, k)
    assert result == 0
