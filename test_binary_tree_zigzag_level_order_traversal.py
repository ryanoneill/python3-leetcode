from binary_tree_zigzag_level_order_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec
from tree_node import TreeNode

def test_ex1():
    root = "[3,9,20,null,null,15,7]"
    codec = Codec()
    head = codec.deserialize(root)

    solution = Solution()
    result = solution.zigzagLevelOrder(head)
    assert result == [[3],[20,9],[15,7]]

def test_ex2():
    root = "[1]"
    codec = Codec()
    head = codec.deserialize(root)

    solution = Solution()
    result = solution.zigzagLevelOrder(head)
    assert result == [[1]]

def test_ex3():
    root = "[]"
    codec = Codec()
    head = codec.deserialize(root)

    solution = Solution()
    result = solution.zigzagLevelOrder(head)
    assert result == []
