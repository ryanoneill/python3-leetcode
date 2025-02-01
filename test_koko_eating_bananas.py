from koko_eating_bananas import Solution

def test_ex1():
    piles = [3,6,7,11]
    h = 8
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    assert result == 4

def test_ex2():
    piles = [30,11,23,4,20]
    h = 5
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    assert result == 30

def test_ex3():
    piles = [30,11,23,4,20]
    h = 6
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    assert result == 23
