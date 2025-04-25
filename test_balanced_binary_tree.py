from balanced_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[3,9,20,null,null,15,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.isBalanced(root)
    assert result


def test_ex2():
    data = "[1,2,2,3,3,null,null,4,4]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.isBalanced(root)
    assert not result


def test_ex3():
    data = "[]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.isBalanced(root)
    assert result
