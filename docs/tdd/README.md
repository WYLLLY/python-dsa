# TDD evidence

The initial structure and the complete 30-problem index precede implementation.
Each batch adds test cases and typed stubs first. Red logs must show behavioral
failures caused by `NotImplementedError`, with successful test collection.
The subsequent implementation is formatted and the complete accumulated suite
is run. Green logs contain that regression result, not just the new tests.

| Batch | Categories | Red | Green |
| --- | --- | --- | --- |
| 01 | Arrays, Hash Maps, Two Pointers | [log](01-red.txt) | [log](01-green.txt) |
| 02 | Sliding Window, Stack | [log](02-red.txt) | [log](02-green.txt) |
| 03 | Linked Lists, Binary Search, Trees | [log](03-red.txt) | [log](03-green.txt) |
| 04 | Graphs, Heaps, Greedy, Dynamic Programming | [log](04-red.txt) | [log](04-green.txt) |

Exact commands and counts are recorded in the final verification report.
