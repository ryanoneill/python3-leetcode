from three_consecutive_odds import Solution

def test_ex1():
    arr = [2,6,4,1]
    solution = Solution()
    result = solution.threeConsecutiveOdds(arr)
    assert not result

def test_ex2():
    arr = [1,2,34,3,4,5,7,23,12]
    solution = Solution()
    result = solution.threeConsecutiveOdds(arr)
    assert result
