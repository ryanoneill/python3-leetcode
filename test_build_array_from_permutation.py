from build_array_from_permutation import Solution

def test_ex1():
    nums = [0,2,1,5,3,4]
    solution = Solution()
    result = solution.buildArray(nums)
    assert result == [0,1,2,4,5,3]

def test_ex2():
    nums = [5,0,1,2,3,4]
    solution = Solution()
    result = solution.buildArray(nums)
    assert result == [4,5,0,1,2,3]
