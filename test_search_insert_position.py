from search_insert_position import Solution


def test_ex1():
    nums = [1, 3, 5, 6]
    target = 5
    solution = Solution()
    result = solution.searchInsert(nums, target)
    assert result == 2


def test_ex2():
    nums = [1, 3, 5, 6]
    target = 2
    solution = Solution()
    result = solution.searchInsert(nums, target)
    assert result == 1


def test_ex3():
    nums = [1, 3, 5, 6]
    target = 7
    solution = Solution()
    result = solution.searchInsert(nums, target)
    assert result == 4
