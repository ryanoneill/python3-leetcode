from check_if_array_is_sorted_and_rotated import Solution

def test_ex1():
    nums = [3,4,5,1,2]
    solution = Solution()
    result = solution.check(nums)
    assert result

def test_ex2():
    nums = [2,1,3,4]
    solution = Solution()
    result = solution.check(nums)
    assert not result

def test_ex3():
    nums = [1,2,3]
    solution = Solution()
    result = solution.check(nums)
    assert result

def test_ex4():
    nums = [6,10,6]
    solution = Solution()
    result = solution.check(nums)
    assert result
