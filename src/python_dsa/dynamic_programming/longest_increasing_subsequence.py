"""Longest Increasing Subsequence.

See problems/dynamic_programming/longest_increasing_subsequence.md.
"""

from bisect import bisect_left


def longest_increasing_subsequence(nums: list[int]) -> int:
    """Return the length of a strictly increasing, noncontiguous subsequence."""
    tails: list[int] = []
    for value in nums:
        index = bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    return len(tails)
