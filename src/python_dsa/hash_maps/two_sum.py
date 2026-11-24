"""Two Sum. See problems/hash_maps/two_sum.md."""


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return a pair of distinct indices, or None when none exists."""
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen.setdefault(value, index)
    return None
