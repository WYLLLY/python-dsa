"""Kth Largest Element. See problems/heaps/kth_largest.md."""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Return the kth largest value counting duplicates, without sorting input."""
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    heap: list[int] = []
    for value in nums:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
