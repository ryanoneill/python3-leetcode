from partition_labels import Solution


def test_ex1():
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    result = solution.partitionLabels(s)
    assert result == [9, 7, 8]


def test_ex2():
    s = "eccbbbbdec"
    solution = Solution()
    result = solution.partitionLabels(s)
    assert result == [10]
