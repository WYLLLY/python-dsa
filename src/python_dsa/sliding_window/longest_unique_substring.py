"""Longest Unique Substring. See problems/sliding_window/longest_unique_substring.md."""


def longest_unique_substring(text: str) -> int:
    """Return the longest contiguous run of distinct code points."""
    last_seen: dict[str, int] = {}
    left = best = 0
    for right, char in enumerate(text):
        left = max(left, last_seen.get(char, -1) + 1)
        best = max(best, right - left + 1)
        last_seen[char] = right
    return best
