from binary_tree_preorder_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    items = "[1,null,2,3]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.preorderTraversal(root)
    assert results == [1, 2, 3]


def test_ex2():
    items = "[1,2,3,4,5,null,8,null,null,6,7,9]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.preorderTraversal(root)
    assert results == [1, 2, 4, 5, 6, 7, 3, 8, 9]


def test_ex3():
    items = "[]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.preorderTraversal(root)
    assert results == []


def test_ex4():
    items = "[1]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.preorderTraversal(root)
    assert results == [1]
