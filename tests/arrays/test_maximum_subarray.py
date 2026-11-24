from copy import deepcopy

import pytest

from python_dsa.arrays.maximum_subarray import maximum_subarray


@pytest.mark.parametrize(
    "args, expected",
    [
        (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
        (([-7, -2, -9],), -2),
        (([5],), 5),
        (([0, 0],), 0),
        (([1, -1, 2],), 2),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert maximum_subarray(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        maximum_subarray(*args)


def test_matches_brute_force():
    from itertools import product

    for size in range(1, 6):
        for values in product((-2, 0, 2), repeat=size):
            expected = max(sum(values[i:j]) for i in range(size) for j in range(i + 1, size + 1))
            assert maximum_subarray(list(values)) == expected
