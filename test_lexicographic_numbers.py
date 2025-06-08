from lexicographic_numbers import Solution

def test_ex1():
    n = 13
    solution = Solution()
    result = solution.lexicalOrder(n)
    assert result == [1,10,11,12,13,2,3,4,5,6,7,8,9]

def test_ex2():
    n = 2
    solution = Solution()
    result = solution.lexicalOrder(n)
    assert result == [1,2]

def test_ex3():
    n = 50000
    solution = Solution()
    result = solution.lexicalOrder(n)
    expected = [i for i in range(1, n+1)]
    expected = sorted(expected, key=lambda x: str(x))
    assert result == expected
