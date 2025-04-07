from sum_root_to_leaf_numbers import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    items = "[1,2,3]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.sumNumbers(root)
    assert result == 25


def test_ex2():
    items = "[4,9,0,5,1]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.sumNumbers(root)
    assert result == 1026
