from count_of_substrings_containing_every_vowel_and_k_consonants_ii import Solution


def test_ex1():
    word = "aeioqq"
    k = 1
    solution = Solution()
    result = solution.countOfSubstrings(word, k)
    assert result == 0


def test_ex2():
    word = "aeiou"
    k = 0
    solution = Solution()
    result = solution.countOfSubstrings(word, k)
    assert result == 1


def test_ex3():
    word = "ieaouqqieaouqq"
    k = 1
    solution = Solution()
    result = solution.countOfSubstrings(word, k)
    assert result == 3


def test_ex4():
    word = "iqeaouqi"
    k = 2
    solution = Solution()
    result = solution.countOfSubstrings(word, k)
    assert result == 3
