from binary_tree_level_order_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    items = "[3,9,20,null,null,15,7]"
    codec = Codec()
    head = codec.deserialize(items)
    solution = Solution()
    result = solution.levelOrder(head)
    assert result == [[3], [9, 20], [15, 7]]


def test_ex2():
    items = "[1]"
    codec = Codec()
    head = codec.deserialize(items)
    solution = Solution()
    result = solution.levelOrder(head)
    assert result == [[1]]


def test_ex3():
    items = "[]"
    codec = Codec()
    head = codec.deserialize(items)
    solution = Solution()
    result = solution.levelOrder(head)
    assert result == []
