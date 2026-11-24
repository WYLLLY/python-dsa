import pytest

from python_dsa.linked_lists.reverse_list import reverse_list
from python_dsa.structures import ListNode


@pytest.mark.parametrize("values", [[], [1], [1, 2, 3], [0, 0], [-2, 0, 4]])
def test_reverses_links_and_reuses_exact_nodes(values):
    original_values = list(values)
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:], strict=False):
        left.next = right
    head = reverse_list(nodes[0] if nodes else None)
    for expected, original_value in zip(reversed(nodes), reversed(original_values), strict=True):
        assert head is expected
        assert head.val == original_value
        head = head.next
    assert head is None


def test_reverse_twice_restores_original_links():
    tail = ListNode(3)
    middle = ListNode(2, tail)
    head = ListNode(1, middle)
    assert reverse_list(reverse_list(head)) is head
    assert head.next is middle
    assert middle.next is tail
    assert tail.next is None
