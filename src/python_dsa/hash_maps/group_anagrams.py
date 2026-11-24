"""Group Anagrams. See problems/hash_maps/group_anagrams.md."""


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words by sorted code points, preserving encounter order."""
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
