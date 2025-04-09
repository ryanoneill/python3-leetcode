from assign_cookies import Solution

def test_ex1():
    g = [1,2,3]
    s = [1,1]
    solution = Solution()
    result = solution.findContentChildren(g, s)
    assert result == 1

def test_ex2():
    g = [1,2]
    s = [1,2,3]
    solution = Solution()
    result = solution.findContentChildren(g, s)
    assert result == 2

def test_ex3():
    g = [10,9,8,7]
    s = [5,6,7,8]
    solution = Solution()
    result = solution.findContentChildren(g, s)
    assert result == 2
