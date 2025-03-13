from zero_array_transformation_ii import Solution

def test_ex1():
    nums = [2,0,2]
    queries = [[0,2,1],[0,2,1],[1,1,3]]
    solution = Solution()
    result = solution.minZeroArray(nums, queries)
    assert result == 2

def test_ex2():
    nums = [4,3,2,1]
    queries = [[1,3,2],[0,2,1]]
    solution = Solution()
    result = solution.minZeroArray(nums, queries)
    assert result == -1
