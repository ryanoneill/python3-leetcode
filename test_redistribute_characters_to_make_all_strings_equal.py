from redistribute_characters_to_make_all_strings_equal import Solution


def test_ex1():
    words = ["abc", "aabc", "bc"]
    solution = Solution()
    result = solution.makeEqual(words)
    assert result


def test_ex2():
    words = ["ab", "a"]
    solution = Solution()
    result = solution.makeEqual(words)
    assert not result
