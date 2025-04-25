from range_sum_of_bst import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[10,5,15,3,7,null,18]"
    codec = Codec()
    root = codec.deserialize(data)
    low = 7
    high = 15
    solution = Solution()
    result = solution.rangeSumBST(root, low, high)
    assert result == 32


def test_ex2():
    data = "[10,5,15,3,7,13,18,1,null,6]"
    codec = Codec()
    root = codec.deserialize(data)
    low = 6
    high = 10
    solution = Solution()
    result = solution.rangeSumBST(root, low, high)
    assert result == 23
