from successful_pairs_of_spells_and_potions import Solution

def test_ex1():
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7  
    solution = Solution()
    result = solution.successfulPairs(spells, potions, success)
    assert result == [4,0,3]

def test_ex2():
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    solution = Solution()
    result = solution.successfulPairs(spells, potions, success)
    assert result == [2,0,2]

