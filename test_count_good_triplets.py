from count_good_triplets import Solution


def test_ex1():
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    solution = Solution()
    result = solution.countGoodTriplets(arr, a, b, c)
    assert result == 4


def test_ex2():
    arr = [1, 1, 2, 2, 3]
    a = 0
    b = 0
    c = 1
    solution = Solution()
    result = solution.countGoodTriplets(arr, a, b, c)
    assert result == 0
