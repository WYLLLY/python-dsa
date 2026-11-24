import pytest

from python_dsa.structures import TreeNode
from python_dsa.trees.validate_bst import validate_bst


@pytest.mark.parametrize(
    "root, expected",
    [
        (None, True),
        (TreeNode(1), True),
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(2, TreeNode(2)), False),
        (TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), False),
        (TreeNode(0, TreeNode(-(10**100)), TreeNode(10**100)), True),
    ],
)
def test_strict_global_ordering(root, expected):
    assert validate_bst(root) is expected


def test_deep_tree_and_preserved_links():
    root = TreeNode(0)
    node = root
    for i in range(1, 2000):
        node.right = TreeNode(i)
        node = node.right
    assert validate_bst(root) is True
    node = root
    for i in range(2000):
        assert node.val == i
        assert node.left is None
        if i < 1999:
            node = node.right
