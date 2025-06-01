from distribute_candies_among_children_ii import Solution

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

# def test_ex3():
#     n = 1000000
#     limit = 1000000
#     solution = Solution()
#     result = solution.distributeCandies(n, limit)
#     assert result == 100
#
