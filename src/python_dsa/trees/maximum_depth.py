"""Maximum Tree Depth. See problems/trees/maximum_depth.md."""

from python_dsa.structures import TreeNode


def maximum_depth(root: TreeNode | None) -> int:
    """Return the longest root-to-leaf node count without recursion."""
    if root is None:
        return 0
    pending = [(root, 1)]
    best = 0
    while pending:
        node, depth = pending.pop()
        best = max(best, depth)
        if node.left is not None:
            pending.append((node.left, depth + 1))
        if node.right is not None:
            pending.append((node.right, depth + 1))
    return best
