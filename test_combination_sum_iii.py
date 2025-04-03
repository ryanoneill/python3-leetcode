from combination_sum_iii import Solution

def test_ex1():
    k = 3
    n = 7
    solution = Solution()
    results = solution.combinationSum3(k, n)
    assert results == [[1,2,4]]

def test_ex2():
    k = 3
    n = 9
    solution = Solution()
    results = solution.combinationSum3(k, n)
    assert results == [[1,2,6], [1,3,5], [2,3,4]]

def test_ex3():
    k = 4
    n = 1
    solution = Solution()
    results = solution.combinationSum3(k, n)
    assert results == []
