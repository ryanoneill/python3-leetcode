from permutations_ii import Solution

def test_ex1():
    nums = [1,1,2]
    solution = Solution()
    results = solution.permuteUnique(nums)
    assert results == [[1,1,2], [1,2,1], [2,1,1]]

def test_ex2():
    nums = [1,2,3]
    solution = Solution()
    results = solution.permuteUnique(nums)
    assert results == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

def test_ex3():
    nums = [3,3,0,3]
    solution = Solution()
    results = solution.permuteUnique(nums)
    assert results == [[0,3,3,3], [3,0,3,3], [3,3,0,3], [3,3,3,0]]
