"""Sliding Window Maximum. See problems/sliding_window/sliding_window_maximum.md."""

from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """Return each width-k maximum using a decreasing index deque."""
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    candidates: deque[int] = deque()
    result: list[int] = []
    for i, value in enumerate(nums):
        while candidates and candidates[0] <= i - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(i)
        if i >= k - 1:
            result.append(nums[candidates[0]])
    return result
