from binary_tree_level_order_traversal_ii import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    items = "[3,9,20,null,null,15,7]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.levelOrderBottom(root)
    assert result == [[15, 7], [9, 20], [3]]


def test_ex2():
    items = "[1]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.levelOrderBottom(root)
    assert result == [[1]]
