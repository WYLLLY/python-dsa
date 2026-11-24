"""Trapping Rain Water. See problems/arrays/trapping_rain_water.md."""


def trapping_rain_water(heights: list[int]) -> int:
    """Return water held between nonnegative unit-width bars."""
    if any(height < 0 for height in heights):
        raise ValueError("heights must be nonnegative")
    left, right = 0, len(heights) - 1
    left_max = right_max = water = 0
    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    return water
