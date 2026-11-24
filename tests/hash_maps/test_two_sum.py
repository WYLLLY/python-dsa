from copy import deepcopy

import pytest

from python_dsa.hash_maps.two_sum import two_sum


@pytest.mark.parametrize(
    "args, expected",
    [
        (([2, 7, 11, 15], 9), (0, 1)),
        (([3, 3], 6), (0, 1)),
        (([1, 2], 8), None),
        (([], 0), None),
        (([-3, 4, 3], 0), (0, 2)),
        (([1], 2), None),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert two_sum(*args) == expected
    assert args == before
