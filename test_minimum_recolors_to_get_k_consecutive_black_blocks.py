from minimum_recolors_to_get_k_consecutive_black_blocks import Solution

def test_ex1():
    blocks = "WBBWWBBWBW"
    k = 7
    solution = Solution()
    result = solution.minimumRecolors(blocks, k)
    assert result == 3

def test_ex2():
    blocks = "WBWBBBW"
    k = 2
    solution = Solution()
    result = solution.minimumRecolors(blocks, k)
    assert result == 0
