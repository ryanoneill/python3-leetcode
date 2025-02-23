from binary_tree_inorder_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    items = "[1,null,2,3]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.inorderTraversal(root)
    assert result == [1,3,2]

def test_ex2():
    items = "[1,2,3,4,5,null,8,null,null,6,7,9]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.inorderTraversal(root)
    assert result == [4,2,6,5,7,1,3,9,8]

def test_ex3():
    items = "[]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.inorderTraversal(root)
    assert result == []

def test_ex4():
    items = "[1]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.inorderTraversal(root)
    assert result == [1]
