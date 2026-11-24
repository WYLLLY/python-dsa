"""Reverse Linked List. See problems/linked_lists/reverse_list.md."""

from python_dsa.structures import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse an acyclic chain in place and return its new head."""
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous, current = current, following
    return previous
