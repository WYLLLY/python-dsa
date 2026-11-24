"""Maximum Subarray. See problems/arrays/maximum_subarray.md."""


def maximum_subarray(nums: list[int]) -> int:
    """Return the greatest sum of a nonempty contiguous slice."""
    if not nums:
        raise ValueError("nums must be nonempty")
    values = iter(nums)
    ending = best = next(values)
    for value in values:
        ending = max(value, ending + value)
        best = max(best, ending)
    return best
