# Python DSA

30 data structures and algorithms exercises in modern, typed Python. Each exercise
pairs an original explanation with a focused implementation and executable pytest
examples, including boundary cases. Practice the pattern, explain the invariant,
then check the complexity.

## Contents

- [Quick start](#quick-start)
- [Study progression](#study-progression)
- [Problem index](#problem-index)
- [Repository layout](#repository-layout)
- [Quality and TDD](#quality-and-tdd)
- [Attribution and license](#attribution-and-license)

## Quick start

Requires Python 3.12 or newer. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install --no-deps -e .
pytest
ruff check .
ruff format --check .
mypy src
```

Run one exercise with `pytest tests/arrays/test_maximum_subarray.py -v`.
Read its problem page before opening the solution. Inputs are not mutated unless
explicitly documented (the linked-list exercises reuse nodes).

## Study progression

1. **Foundations:** Hash Maps, Two Pointers, Binary Search, Linked Lists, easy Stack
   and Trees exercises. Trace an example and name the maintained invariant.
2. **Core patterns:** Arrays, Sliding Window, monotonic Stack, BFS/DFS, Heaps and
   Greedy. Contrast the optimized algorithm with a brute-force approach.
3. **Dynamic Programming:** start with Climbing Stairs, then Coin Change and LIS.
4. **Stretch:** Trapping Rain Water, Minimum Window Substring, Sliding Window
   Maximum and Largest Rectangle. Revisit them without looking at the solution.

Difficulty labels follow the linked canonical problems; this repository defines
its own explicit contracts, which can differ on empty and invalid inputs.

**Implementation progress: 30/30** — 9 Easy, 17 Medium, 4 Hard.

## Problem index

| # | Problem | Category | Difficulty | Status |
| --- | --- | --- | --- | --- |
| 01 | [Maximum Subarray](problems/arrays/maximum_subarray.md) | Arrays | Medium | Complete |
| 02 | [Product Except Self](problems/arrays/product_except_self.md) | Arrays | Medium | Complete |
| 03 | [Trapping Rain Water](problems/arrays/trapping_rain_water.md) | Arrays | Hard | Complete |
| 04 | [Two Sum](problems/hash_maps/two_sum.md) | Hash Maps | Easy | Complete |
| 05 | [Valid Anagram](problems/hash_maps/valid_anagram.md) | Hash Maps | Easy | Complete |
| 06 | [Group Anagrams](problems/hash_maps/group_anagrams.md) | Hash Maps | Medium | Complete |
| 07 | [Valid Palindrome](problems/two_pointers/valid_palindrome.md) | Two Pointers | Easy | Complete |
| 08 | [Container With Most Water](problems/two_pointers/container_with_most_water.md) | Two Pointers | Medium | Complete |
| 09 | [Longest Unique Substring](problems/sliding_window/longest_unique_substring.md) | Sliding Window | Medium | Complete |
| 10 | [Minimum Window Substring](problems/sliding_window/minimum_window_substring.md) | Sliding Window | Hard | Complete |
| 11 | [Sliding Window Maximum](problems/sliding_window/sliding_window_maximum.md) | Sliding Window | Hard | Complete |
| 12 | [Valid Parentheses](problems/stack/valid_parentheses.md) | Stack | Easy | Complete |
| 13 | [Daily Temperatures](problems/stack/daily_temperatures.md) | Stack | Medium | Complete |
| 14 | [Largest Rectangle in Histogram](problems/stack/largest_rectangle.md) | Stack | Hard | Complete |
| 15 | [Reverse Linked List](problems/linked_lists/reverse_list.md) | Linked Lists | Easy | Complete |
| 16 | [Merge Two Sorted Lists](problems/linked_lists/merge_sorted_lists.md) | Linked Lists | Easy | Complete |
| 17 | [Binary Search](problems/binary_search/binary_search.md) | Binary Search | Easy | Complete |
| 18 | [Search Rotated Sorted Array](problems/binary_search/search_rotated.md) | Binary Search | Medium | Complete |
| 19 | [Maximum Tree Depth](problems/trees/maximum_depth.md) | Trees | Easy | Complete |
| 20 | [Validate Binary Search Tree](problems/trees/validate_bst.md) | Trees | Medium | Complete |
| 21 | [Binary Tree Level Order](problems/trees/level_order.md) | Trees | Medium | Complete |
| 22 | [Number of Islands](problems/graphs/number_of_islands.md) | Graphs | Medium | Complete |
| 23 | [Course Schedule](problems/graphs/course_schedule.md) | Graphs | Medium | Complete |
| 24 | [Kth Largest Element](problems/heaps/kth_largest.md) | Heaps | Medium | Complete |
| 25 | [Top K Frequent Elements](problems/heaps/top_k_frequent.md) | Heaps | Medium | Complete |
| 26 | [Jump Game](problems/greedy/jump_game.md) | Greedy | Medium | Complete |
| 27 | [Merge Intervals](problems/greedy/merge_intervals.md) | Greedy | Medium | Complete |
| 28 | [Climbing Stairs](problems/dynamic_programming/climbing_stairs.md) | Dynamic Programming | Easy | Complete |
| 29 | [Coin Change](problems/dynamic_programming/coin_change.md) | Dynamic Programming | Medium | Complete |
| 30 | [Longest Increasing Subsequence](problems/dynamic_programming/longest_increasing_subsequence.md) | Dynamic Programming | Medium | Complete |

## Repository layout

```text
src/python_dsa/<category>/<problem>.py  # typed solution
src/python_dsa/structures.py           # shared linked-list and tree nodes
tests/<category>/test_<problem>.py     # examples, edge cases and small oracles
problems/<category>/<problem>.md       # statement, reasoning, complexity, source
docs/tdd/                             # recorded Red and Green terminal output
docs/verification.md                  # final checks and scope
```

## Quality and TDD

Each implementation batch starts with importable function signatures that raise
`NotImplementedError`. Behavioral tests are executed and their failures recorded
before solutions are written. Small test commits are followed by implementation
commits; Ruff formatting is the refactor step. See [the TDD record](docs/tdd/README.md) and [verification report](docs/verification.md).
GitHub Actions runs pytest, Ruff lint/format and mypy on Python 3.12, 3.13 and 3.14.
No database, web service or external API is part of this project.

## Attribution and license

The exercises are inspired by classic interview patterns, with a canonical
LeetCode link on every problem page. Statements are rewritten for this repository;
implementations, explanations and tests were authored for this project with
OpenAI Codex assistance. No third-party solution code was copied. The source links
identify problem provenance, not a claim of affiliation or ownership of the
underlying algorithm. Repository code and original prose are under [MIT](LICENSE).
