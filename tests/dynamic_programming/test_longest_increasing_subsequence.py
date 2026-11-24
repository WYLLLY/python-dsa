from copy import deepcopy

import pytest

from python_dsa.dynamic_programming.longest_increasing_subsequence import (
    longest_increasing_subsequence,
)


@pytest.mark.parametrize(
    "args, expected",
    [
        (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
        (([],), 0),
        (([7, 7, 7],), 1),
        (([5, 4, 3],), 1),
        (([-3, -2, -1],), 3),
        (([0, 1, 0, 3, 2, 3],), 4),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert longest_increasing_subsequence(*args) == expected
    assert args == before


def test_matches_subsequence_enumeration():
    from itertools import combinations, product

    for size in range(6):
        for values in product(range(3), repeat=size):
            expected = max(
                (
                    len(sub)
                    for length in range(size + 1)
                    for sub in combinations(values, length)
                    if all(a < b for a, b in zip(sub, sub[1:], strict=False))
                ),
                default=0,
            )
            assert longest_increasing_subsequence(list(values)) == expected
