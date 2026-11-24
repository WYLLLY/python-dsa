"""Valid Anagram. See problems/hash_maps/valid_anagram.md."""

from collections import Counter


def valid_anagram(left: str, right: str) -> bool:
    """Compare exact Unicode code-point multiplicities."""
    return Counter(left) == Counter(right)
