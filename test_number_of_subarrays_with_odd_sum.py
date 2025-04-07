from number_of_subarrays_with_odd_sum import Solution


def test_ex1():
    arr = [1, 3, 5]
    solution = Solution()
    result = solution.numOfSubarrays(arr)
    assert result == 4


def test_ex2():
    arr = [2, 4, 6]
    solution = Solution()
    result = solution.numOfSubarrays(arr)
    assert result == 0


def test_ex3():
    arr = [1, 2, 3, 4, 5, 6, 7]
    solution = Solution()
    result = solution.numOfSubarrays(arr)
    assert result == 16
