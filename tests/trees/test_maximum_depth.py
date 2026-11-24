import pytest

from python_dsa.structures import TreeNode
from python_dsa.trees.maximum_depth import maximum_depth


@pytest.mark.parametrize(
    "root, expected",
    [
        (None, 0),
        (TreeNode(1), 1),
        (TreeNode(1, TreeNode(2), TreeNode(3)), 2),
        (TreeNode(1, None, TreeNode(2, TreeNode(3))), 3),
    ],
)
def test_depth(root, expected):
    assert maximum_depth(root) == expected


def test_deep_tree_is_iterative_and_not_mutated():
    root = TreeNode(0)
    node = root
    for i in range(1, 2000):
        node.left = TreeNode(i)
        node = node.left
    assert maximum_depth(root) == 2000
    node = root
    for i in range(2000):
        assert node.val == i
        assert node.right is None
        if i < 1999:
            node = node.left
