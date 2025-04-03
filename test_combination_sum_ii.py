from combination_sum_ii import Solution

def test_ex1():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solution = Solution()
    results = solution.combinationSum2(candidates, target)
    # results = map(sorted, results)
    # results = sorted(results)
    assert results == [[1,1,6], [1,2,5], [1,7], [2,6]]

def test_ex2():
    candidates = [2,5,2,1,2]
    target = 5
    solution = Solution()
    results = solution.combinationSum2(candidates, target)
    # results = map(sorted, results)
    # results = sorted(results)
    assert results == [[1,2,2], [5]]
