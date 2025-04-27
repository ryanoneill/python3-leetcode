from exclusive_time_of_functions import Solution

def test_ex1():
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    solution = Solution()
    result = solution.exclusiveTime(n, logs)
    assert result == [3,4]

def test_ex2():
    n = 1
    logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    solution = Solution()
    result = solution.exclusiveTime(n, logs)
    assert result == [8]

def test_ex3():
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    solution = Solution()
    result = solution.exclusiveTime(n, logs)
    assert result == [7,1]
