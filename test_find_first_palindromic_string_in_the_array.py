from find_first_palindromic_string_in_the_array import Solution


def test_ex1():
    words = ["abc", "car", "ada", "racecar", "cool"]
    solution = Solution()
    result = solution.firstPalindrome(words)
    assert result == "ada"


def test_ex2():
    words = ["notapalindrome", "racecar"]
    solution = Solution()
    result = solution.firstPalindrome(words)
    assert result == "racecar"


def test_ex3():
    words = ["def", "ghi"]
    solution = Solution()
    result = solution.firstPalindrome(words)
    assert result == ""
