# Product Except Self

**Arrays · Medium**

## Problem

For each index, return the product of every other element, without division. The empty input gives `[]`; a singleton gives `[1]` (empty product). Zeros and negative integers are allowed.

```python
product_except_self(nums: list[int]) -> list[int]
```

`product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]`.

## Reasoning

First store each strict prefix product in the output. Scan backward while maintaining a strict suffix product. Their product excludes exactly the current entry. No special handling of zero is needed.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1), excluding the O(n) output.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/arrays/product_except_self.py)
- [pytest tests](../../tests/arrays/test_product_except_self.py)
- Run: `pytest tests/arrays/test_product_except_self.py -v`

## Attribution

Problem inspiration: [LeetCode — Product Except Self](https://leetcode.com/problems/product-of-array-except-self/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
