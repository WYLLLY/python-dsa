"""Climbing Stairs. See problems/dynamic_programming/climbing_stairs.md."""


def climbing_stairs(n: int) -> int:
    """Count ordered ways to climb n stairs with steps of size 1 or 2."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    previous, current = 1, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
