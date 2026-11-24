from copy import deepcopy

import pytest

from python_dsa.sliding_window.sliding_window_maximum import sliding_window_maximum


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([2, 2, 2], 2), [2, 2]),
        (([-4, -2], 1), [-4, -2]),
        (([3, 1], 2), [3]),
        (([7], 1), [7]),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert sliding_window_maximum(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([], 1), ([1], 0), ([1], 2), ([1], -1)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        sliding_window_maximum(*args)


def test_matches_brute_force():
    from itertools import product

    for size in range(1, 6):
        for values in product((-1, 0, 1), repeat=size):
            for k in range(1, size + 1):
                expected = [max(values[i : i + k]) for i in range(size - k + 1)]
                assert sliding_window_maximum(list(values), k) == expected
