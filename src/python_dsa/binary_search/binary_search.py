"""Binary Search. See problems/binary_search/binary_search.md."""


def binary_search(nums: list[int], target: int) -> int:
    """Search a strictly increasing array, returning -1 if absent."""
    left, right = 0, len(nums)
    while left < right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle
    return -1
