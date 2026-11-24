"""Top K Frequent Elements. See problems/heaps/top_k_frequent.md."""

import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return k most frequent values, ties ordered by smaller value."""
    counts = Counter(nums)
    if not 0 <= k <= len(counts):
        raise ValueError("k must be between 0 and the distinct value count")
    return heapq.nsmallest(k, counts, key=lambda value: (-counts[value], value))
