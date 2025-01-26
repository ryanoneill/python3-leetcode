from tree_node import TreeNode
from minimum_depth_of_binary_tree import Solution

# TODO: implement Codec for serialization and deserialization of binary tree

def test_ex1():
    head = TreeNode(3)
    nine = TreeNode(9)
    head.left = nine
    twenty = TreeNode(20)
    head.right = twenty
    fifteen = TreeNode(15)
    twenty.left = fifteen
    seven = TreeNode(7)
    twenty.right = seven

    solution = Solution()
    result = solution.minDepth(head)
    assert result == 2

def test_ex2():
    head = TreeNode(2)
    three = TreeNode(3)
    head.right = three
    four = TreeNode(4)
    three.right = four
    five = TreeNode(5)
    four.right = five
    six = TreeNode(6)
    five.right = six

    solution = Solution()
    result = solution.minDepth(head)
    assert result == 5

