from hand_of_straights import Solution

def test_ex1():
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    solution = Solution()
    result = solution.isNStraightHand(hand, groupSize)
    assert result

def test_ex2():
    hand = [1,2,3,4,5]
    groupSize = 4
    solution = Solution()
    result = solution.isNStraightHand(hand, groupSize)
    assert not result
