from copy import deepcopy

import pytest

from python_dsa.arrays.product_except_self import product_except_self


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([0, 2, 0],), [0, 0, 0]),
        (([-1, 2, -3],), [-6, 3, -2]),
        (([],), []),
        (([7],), [1]),
        (([0, 2, 3],), [6, 0, 0]),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert product_except_self(*args) == expected
    assert args == before


def test_matches_brute_force():
    from itertools import product
    from math import prod

    for size in range(5):
        for values in product((-1, 0, 2), repeat=size):
            expected = [prod(values[:i] + values[i + 1 :]) for i in range(size)]
            assert product_except_self(list(values)) == expected
