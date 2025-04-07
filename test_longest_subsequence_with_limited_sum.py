from longest_subsequence_with_limited_sum import Solution


def test_ex1():
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    solution = Solution()
    result = solution.answerQueries(nums, queries)
    assert result == [2, 3, 4]


def test_ex2():
    nums = [2, 3, 4, 5]
    queries = [1]
    solution = Solution()
    result = solution.answerQueries(nums, queries)
    assert result == [0]
