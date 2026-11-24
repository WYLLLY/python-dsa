"""Minimum Window Substring. See problems/sliding_window/minimum_window_substring.md."""

from collections import Counter


def minimum_window_substring(text: str, required: str) -> str:
    """Return the shortest covering substring, breaking ties leftmost."""
    if not required:
        return ""
    needed = Counter(required)
    missing = len(required)
    left = best_start = 0
    best_length = len(text) + 1
    for right, char in enumerate(text):
        if needed[char] > 0:
            missing -= 1
        needed[char] -= 1
        while missing == 0:
            length = right - left + 1
            if length < best_length:
                best_start, best_length = left, length
            departing = text[left]
            needed[departing] += 1
            if needed[departing] > 0:
                missing += 1
            left += 1
    if best_length > len(text):
        return ""
    return text[best_start : best_start + best_length]
