from reverse_words_in_a_string_iii import Solution


def test_ex1():
    s = "Let's take LeetCode contest"
    solution = Solution()
    result = solution.reverseWords(s)
    assert result == "s'teL ekat edoCteeL tsetnoc"


def test_ex2():
    s = "Mr Ding"
    solution = Solution()
    result = solution.reverseWords(s)
    assert result == "rM gniD"
