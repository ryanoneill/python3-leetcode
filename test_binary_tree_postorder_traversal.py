from binary_tree_postorder_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    items = "[1,null,2,3]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.postorderTraversal(root)
    assert results == [3, 2, 1]


def test_ex2():
    items = "[1,2,3,4,5,null,8,null,null,6,7,9]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.postorderTraversal(root)
    assert results == [4, 6, 7, 5, 2, 9, 8, 3, 1]


def test_ex3():
    items = "[]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.postorderTraversal(root)
    assert results == []


def test_ex4():
    items = "[1]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    results = solution.postorderTraversal(root)
    assert results == [1]
