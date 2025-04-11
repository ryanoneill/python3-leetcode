from height_checker import Solution

def test_ex1():
    heights = [1,1,4,2,1,3]
    solution = Solution()
    result = solution.heightChecker(heights)
    assert result == 3

def test_ex2():
    heights = [5,1,2,3,4]
    solution = Solution()
    result = solution.heightChecker(heights)
    assert result == 5

def test_ex3():
    heights = [1,2,3,4,5]
    solution = Solution()
    result = solution.heightChecker(heights)
    assert result == 0
