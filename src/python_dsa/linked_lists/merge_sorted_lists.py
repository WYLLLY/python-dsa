"""Merge Two Sorted Lists. See problems/linked_lists/merge_sorted_lists.md."""

from python_dsa.structures import ListNode


def merge_sorted_lists(left: ListNode | None, right: ListNode | None) -> ListNode | None:
    """Splice two sorted, acyclic, disjoint chains; prefer left on ties."""
    dummy = ListNode(0)
    tail = dummy
    while left is not None and right is not None:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left is not None else right
    return dummy.next
