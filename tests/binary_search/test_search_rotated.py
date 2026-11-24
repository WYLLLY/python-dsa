from copy import deepcopy

import pytest

from python_dsa.binary_search.search_rotated import search_rotated


@pytest.mark.parametrize(
    "args, expected",
    [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([], 0), -1),
        (([1], 1), 0),
        (([1, 2, 3], 3), 2),
        (([3, 1], 1), 1),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert search_rotated(*args) == expected
    assert args == before


def test_all_rotations_and_missing_targets():
    for size in range(9):
        values = list(range(0, size * 2, 2))
        for pivot in range(max(1, size)):
            rotated = values[pivot:] + values[:pivot]
            for target in range(-1, size * 2 + 1):
                expected = rotated.index(target) if target in rotated else -1
                assert search_rotated(rotated, target) == expected
