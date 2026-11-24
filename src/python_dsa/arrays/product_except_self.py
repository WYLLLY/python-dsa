"""Product Except Self. See problems/arrays/product_except_self.md."""


def product_except_self(nums: list[int]) -> list[int]:
    """Return products of all other entries, without division."""
    result = [1] * len(nums)
    prefix = 1
    for i, value in enumerate(nums):
        result[i] = prefix
        prefix *= value
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
