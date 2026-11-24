import pytest

from python_dsa.linked_lists.merge_sorted_lists import merge_sorted_lists
from python_dsa.structures import ListNode


@pytest.mark.parametrize(
    "left_values, right_values",
    [([], []), ([1], []), ([], [2]), ([1, 2, 4], [1, 3, 4]), ([-3, 0], [-2, 0, 2]), ([1, 1], [1])],
)
def test_merges_reusing_nodes_and_left_first_on_ties(left_values, right_values):
    left = [ListNode(value) for value in left_values]
    right = [ListNode(value) for value in right_values]
    for chain in (left, right):
        for a, b in zip(chain, chain[1:], strict=False):
            a.next = b
    expected = sorted(((node, node.val) for node in left + right), key=lambda pair: pair[1])
    head = merge_sorted_lists(left[0] if left else None, right[0] if right else None)
    for node, original_value in expected:
        assert head is node
        assert head.val == original_value
        head = head.next
    assert head is None
