"""Largest Rectangle in Histogram. See problems/stack/largest_rectangle.md."""


def largest_rectangle(heights: list[int]) -> int:
    """Return the largest rectangle under nonnegative unit-width bars."""
    if any(height < 0 for height in heights):
        raise ValueError("heights must be nonnegative")
    stack: list[tuple[int, int]] = []
    best = 0
    for i in range(len(heights) + 1):
        height = heights[i] if i < len(heights) else 0
        start = i
        while stack and stack[-1][1] > height:
            start, previous = stack.pop()
            best = max(best, previous * (i - start))
        if not stack or stack[-1][1] < height:
            stack.append((start, height))
    return best
