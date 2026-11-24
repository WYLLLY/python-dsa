"""Search Rotated Sorted Array. See problems/binary_search/search_rotated.md."""


def search_rotated(nums: list[int], target: int) -> int:
    """Search a rotation of a strictly increasing array."""
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif nums[middle] < target <= nums[right]:
            left = middle + 1
        else:
            right = middle - 1
    return -1
