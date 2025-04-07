from recover_a_tree_from_preorder_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    traversal = "1-2--3--4-5--6--7"
    solution = Solution()
    result = solution.recoverFromPreorder(traversal)
    codec = Codec()
    values = codec.serialize(result)
    assert values == "[1,2,5,3,4,6,7]"


def test_ex2():
    traversal = "1-2--3---4-5--6---7"
    solution = Solution()
    result = solution.recoverFromPreorder(traversal)
    codec = Codec()
    values = codec.serialize(result)
    assert values == "[1,2,5,3,null,6,null,4,null,7]"


def test_ex3():
    traversal = "1-401--349---90--88"
    solution = Solution()
    result = solution.recoverFromPreorder(traversal)
    codec = Codec()
    values = codec.serialize(result)
    assert values == "[1,401,null,349,88,90]"
