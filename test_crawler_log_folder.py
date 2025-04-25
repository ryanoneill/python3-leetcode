from crawler_log_folder import Solution


def test_ex1():
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    solution = Solution()
    result = solution.minOperations(logs)
    assert result == 2


def test_ex2():
    logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
    solution = Solution()
    result = solution.minOperations(logs)
    assert result == 3


def test_ex3():
    logs = ["d1/", "../", "../", "../"]
    solution = Solution()
    result = solution.minOperations(logs)
    assert result == 0
