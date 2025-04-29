from fibonacci_number import Solution

def test_ex1():
    n = 2
    solution = Solution()
    result = solution.fib(n)
    assert result == 1

def test_ex2():
    n = 3
    solution = Solution()
    result = solution.fib(n)
    assert result == 2

def test_ex3():
    n = 4
    solution = Solution()
    result = solution.fib(n)
    assert result == 3
