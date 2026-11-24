from copy import deepcopy

import pytest

from python_dsa.heaps.kth_largest import kth_largest


@pytest.mark.parametrize(
    "args, expected",
    [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
        (([-4, -2, -9], 2), -4),
        (([1], 1), 1),
        (([2, 2], 2), 2),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert kth_largest(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([], 1), ([1], 0), ([1], 2)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        kth_largest(*args)
