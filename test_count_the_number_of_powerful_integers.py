from count_the_number_of_powerful_integers import Solution

def test_ex1():
    start = 1
    finish = 6000
    limit = 4
    s = "124"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 5

def test_ex2():
    start = 15
    finish = 215
    limit = 6
    s = "10"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 2

def test_ex3():
    start = 1000
    finish = 2000
    limit = 4
    s = "3000"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 0

def test_ex4():
    start = 1829505
    finish = 1255574165
    limit = 7
    s = "11223"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 5470 

def test_ex5():
    start = 1114
    finish = 1864854501
    limit = 7
    s = "27"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 4194295

def test_ex6():
    start = 1
    finish = 971
    limit = 9
    s = "41"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 10

def test_ex7():
    start = 3
    finish = 1429
    limit = 5
    s = "11"
    solution = Solution()
    result = solution.numberOfPowerfulInt(start, finish, limit, s)
    assert result == 11
