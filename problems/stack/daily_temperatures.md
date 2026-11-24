# Daily Temperatures

**Stack · Medium**

## Problem

For each day, return how many days must pass until a strictly warmer reading. Use zero if there is none. Readings are arbitrary integers; equal readings do not qualify. Empty input gives `[]`.

```python
daily_temperatures(temperatures: list[int]) -> list[int]
```

`daily_temperatures([30, 40, 35, 50]) == [1, 2, 1, 0]`.

## Reasoning

Store unresolved days in a stack with nonincreasing temperatures. A new warmer day resolves every colder day at the top. These are their first warmer days because no intervening day removed them. Every day is pushed and popped at most once.

## Complexity

**Time:** O(n). **Auxiliary space:** O(n), plus the O(n) output.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/stack/daily_temperatures.py)
- [pytest tests](../../tests/stack/test_daily_temperatures.py)
- Run: `pytest tests/stack/test_daily_temperatures.py -v`

## Attribution

Problem inspiration: [LeetCode — Daily Temperatures](https://leetcode.com/problems/daily-temperatures/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
