from simplify_path import Solution

def test_ex1():
    path = "/home/"
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == "/home"

def test_ex2():
    path = "/home//foo"
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == "/home/foo"

def test_ex3():
    path = "/home/user/Documents/../Pictures"
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == "/home/user/Pictures"

def test_ex4():
    path = "/../"
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == "/"

def test_ex5():
    path = "/.../a/../b/c/../d/./"
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == "/.../b/d"
