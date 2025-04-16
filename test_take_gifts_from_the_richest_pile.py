from take_gifts_from_the_richest_pile import Solution

def test_ex1():
    gifts = [25,64,9,4,100]
    k = 4
    solution = Solution()
    result = solution.pickGifts(gifts, k)
    assert result == 29

def test_ex2():
    gifts = [1,1,1,1]
    k = 4
    solution = Solution()
    result = solution.pickGifts(gifts, k)
    assert result == 4
