from sliding_window_maximum import Solution

def test_ex1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    results = solution.maxSlidingWindow(nums, k)
    assert results == [3,3,5,5,6,7]

def test_ex2():
    nums = [1]
    k = 1
    solution = Solution()
    results = solution.maxSlidingWindow(nums, k)
    assert results == [1]

def test_ex3():
    nums = [1,-1]
    k = 1
    solution = Solution()
    results = solution.maxSlidingWindow(nums, k)
    assert results == [1,-1]
