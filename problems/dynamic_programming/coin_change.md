# Coin Change

**Dynamic Programming · Medium**

## Problem

Using unlimited copies of each positive integer denomination, return the minimum number of coins summing to `amount`, or `-1` if impossible. Zero amount needs zero coins, including with no denominations. Duplicate denominations are allowed. Raise `ValueError` for a negative amount or any nonpositive denomination, even when amount is zero.

```python
coin_change(coins: list[int], amount: int) -> int
```

`coin_change([1, 3, 4], 6) == 2`, using two 3s rather than the greedy choice 4 + 1 + 1.

## Reasoning

Let `best[t]` be the smallest count for total t. Try every denomination as the last coin, using the already solved smaller total `t − coin`. Initialize zero to zero and other totals to an unreachable sentinel larger than any feasible coin count. Positive denominations ensure the recurrence uses earlier states.

## Complexity

For A = amount and C denominations, **time:** O(C + A·(C + 1)), including validation and empty coin lists. **Auxiliary space:** O(A + 1). This is pseudo-polynomial in the numeric amount.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/dynamic_programming/coin_change.py)
- [pytest tests](../../tests/dynamic_programming/test_coin_change.py)
- Run: `pytest tests/dynamic_programming/test_coin_change.py -v`

## Attribution

Problem inspiration: [LeetCode — Coin Change](https://leetcode.com/problems/coin-change/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
