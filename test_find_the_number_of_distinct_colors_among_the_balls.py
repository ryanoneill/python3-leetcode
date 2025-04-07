from find_the_number_of_distinct_colors_among_the_balls import Solution


def test_ex1():
    limit = 4
    queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
    solution = Solution()
    results = solution.queryResults(limit, queries)
    assert results == [1, 2, 2, 3]


def test_ex2():
    limit = 4
    queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    solution = Solution()
    results = solution.queryResults(limit, queries)
    assert results == [1, 2, 2, 3, 4]
