from find_if_array_can_be_sorted import Solution

def test_ex1():
    nums = [8,4,2,30,15]
    solution = Solution()
    result = solution.canSortArray(nums)
    assert result

def test_ex2():
    nums = [1,2,3,4,5]
    solution = Solution()
    result = solution.canSortArray(nums)
    assert result

def test_ex3():
    nums = [3,16,8,4,2]
    solution = Solution()
    result = solution.canSortArray(nums)
    assert not result

def test_ex4():
    nums = [20,16]
    solution = Solution()
    result = solution.canSortArray(nums)
    assert not result
