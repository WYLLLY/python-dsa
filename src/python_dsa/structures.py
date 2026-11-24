"""Minimal mutable nodes shared by the linked-list and tree exercises.

Nodes use identity equality. Algorithms assume finite acyclic structures;
merge_sorted_lists additionally requires the two input chains to be disjoint.
"""

from dataclasses import dataclass


@dataclass(slots=True, eq=False)
class ListNode:
    """A singly linked integer node."""

    val: int
    next: ListNode | None = None


@dataclass(slots=True, eq=False)
class TreeNode:
    """An integer binary-tree node."""

    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None
