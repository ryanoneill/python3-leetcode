from longest_nice_subarray import Solution


def test_ex1():
    nums = [1, 3, 8, 48, 10]
    solution = Solution()
    result = solution.longestNiceSubarray(nums)
    assert result == 3


def test_ex2():
    nums = [3, 1, 5, 11, 13]
    solution = Solution()
    result = solution.longestNiceSubarray(nums)
    assert result == 1


def test_ex3():
    nums = [
        84139415,
        693324769,
        614626365,
        497710833,
        615598711,
        264,
        65552,
        50331652,
        1,
        1048576,
        16384,
        544,
        270532608,
        151813349,
        221976871,
        678178917,
        845710321,
        751376227,
        331656525,
        739558112,
        267703680,
    ]
    solution = Solution()
    result = solution.longestNiceSubarray(nums)
    assert result == 8
