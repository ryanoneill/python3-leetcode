from minimum_bit_flips_to_convert_number import Solution

def test_ex1():
    start = 10
    goal = 7
    solution = Solution()
    result = solution.minBitFlips(start, goal)
    assert result == 3

def test_ex2():
    start = 3
    goal = 4
    solution = Solution()
    result = solution.minBitFlips(start, goal)
    assert result == 3
