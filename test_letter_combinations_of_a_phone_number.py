from letter_combinations_of_a_phone_number import Solution


def test_ex1():
    digits = "23"
    solution = Solution()
    result = solution.letterCombinations(digits)
    result.sort()
    assert result == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_ex2():
    digits = ""
    solution = Solution()
    result = solution.letterCombinations(digits)
    result.sort()
    assert result == []


def test_ex3():
    digits = "2"
    solution = Solution()
    result = solution.letterCombinations(digits)
    result.sort()
    assert result == ["a", "b", "c"]
