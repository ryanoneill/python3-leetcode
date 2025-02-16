from check_if_one_string_swap_can_make_strings_equal import Solution

def test_ex1():
    s1 = "bank"
    s2 = "kanb"
    solution = Solution()
    result = solution.areAlmostEqual(s1, s2)
    assert result

def test_ex2():
    s1 = "attack"
    s2 = "defend"
    solution = Solution()
    result = solution.areAlmostEqual(s1, s2)
    assert not result

def test_ex3():
    s1 = "kelb"
    s2 = "kelb"
    solution = Solution()
    result = solution.areAlmostEqual(s1, s2)
    assert result
