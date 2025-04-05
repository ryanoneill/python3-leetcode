from single_number import Solution

def test_ex1():
    nums = [2,2,1]
    solution = Solution()
    result = solution.singleNumber(nums)
    assert result == 1

def test_ex2():
    nums = [4,1,2,1,2]
    solution = Solution()
    result = solution.singleNumber(nums)
    assert result == 4

def test_ex3():
    nums = [1]
    solution = Solution()
    result = solution.singleNumber(nums)
    assert result == 1
