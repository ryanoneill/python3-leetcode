from permutations import Solution

def test_ex1():
    nums = [1,2,3]
    solution = Solution()
    results = solution.permute(nums)
    assert results == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def test_ex2():
    nums = [0,1]
    solution = Solution()
    results = solution.permute(nums)
    assert results == [[0,1],[1,0]]

def test_ex3():
    nums = [1]
    solution = Solution()
    results = solution.permute(nums)
    assert results == [[1]]
