"""Container With Most Water. See problems/two_pointers/container_with_most_water.md."""


def container_with_most_water(heights: list[int]) -> int:
    """Return the greatest area between two vertical lines."""
    if any(height < 0 for height in heights):
        raise ValueError("heights must be nonnegative")
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(heights[left], heights[right]))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best
