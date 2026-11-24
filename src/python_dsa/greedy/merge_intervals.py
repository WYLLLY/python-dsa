"""Merge Intervals. See problems/greedy/merge_intervals.md."""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or touching closed intervals without input mutation."""
    if any(start > end for start, end in intervals):
        raise ValueError("interval start must not exceed end")
    merged: list[tuple[int, int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged
