from kth_distinct_string_in_an_array import Solution


def test_ex1():
    arr = ["d", "b", "c", "b", "c", "a"]
    k = 2
    solution = Solution()
    result = solution.kthDistinct(arr, k)
    assert result == "a"


def test_ex2():
    arr = ["aaa", "aa", "a"]
    k = 1
    solution = Solution()
    result = solution.kthDistinct(arr, k)
    assert result == "aaa"


def test_ex3():
    arr = ["a", "b", "a"]
    k = 3
    solution = Solution()
    result = solution.kthDistinct(arr, k)
    assert result == ""
