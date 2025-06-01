from distribute_candies_among_children_i import Solution

def test_ex1():
    n = 5
    limit = 2
    solution = Solution()
    result = solution.distributeCandies(n, limit)
    assert result == 3

def test_ex2():
    n = 3
    limit = 3
    solution = Solution()
    result = solution.distributeCandies(n, limit)
    assert result == 10
