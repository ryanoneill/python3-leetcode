from diameter_of_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    root = "[1,2,3,4,5]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.diameterOfBinaryTree(head)
    assert result == 3


def test_ex2():
    root = "[1,2]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.diameterOfBinaryTree(head)
    assert result == 1
