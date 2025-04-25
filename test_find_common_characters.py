from find_common_characters import Solution


def test_ex1():
    words = ["bella", "label", "roller"]
    solution = Solution()
    results = solution.commonChars(words)
    results.sort()
    assert results == ["e", "l", "l"]


def test_ex2():
    words = ["cool", "lock", "cook"]
    solution = Solution()
    results = solution.commonChars(words)
    results.sort()
    assert results == ["c", "o"]
