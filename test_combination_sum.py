from combination_sum import Solution

def test_ex1():
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    results = solution.combinationSum(candidates, target)
    assert results == [[2,2,3], [7]]

def test_ex2():
    candidates = [2,3,5]
    target = 8
    solution = Solution()
    results = solution.combinationSum(candidates, target)
    assert results == [[2,2,2,2], [2,3,3], [3,5]]

def test_ex3():
    candidates = [2]
    target = 1
    solution = Solution()
    results = solution.combinationSum(candidates, target)
    assert results == []
