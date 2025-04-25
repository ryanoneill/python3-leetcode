from string_matching_in_an_array import Solution


def test_ex1():
    words = ["mass", "as", "hero", "superhero"]
    solution = Solution()
    results = solution.stringMatching(words)
    assert results == ["as", "hero"]


def test_ex2():
    words = ["leetcode", "et", "code"]
    solution = Solution()
    results = solution.stringMatching(words)
    assert results == ["et", "code"]


def test_ex3():
    words = ["blue", "green", "bu"]
    solution = Solution()
    results = solution.stringMatching(words)
    assert results == []
