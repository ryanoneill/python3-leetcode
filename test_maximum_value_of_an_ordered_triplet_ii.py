from maximum_value_of_an_ordered_triplet_ii import Solution


def test_ex1():
    nums = [12, 6, 1, 2, 7]
    solution = Solution()
    result = solution.maximumTripletValue(nums)
    assert result == 77


def test_ex2():
    nums = [1, 10, 3, 4, 19]
    solution = Solution()
    result = solution.maximumTripletValue(nums)
    assert result == 133


def test_ex3():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.maximumTripletValue(nums)
    assert result == 0
