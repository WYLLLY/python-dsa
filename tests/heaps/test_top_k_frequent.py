from copy import deepcopy

import pytest

from python_dsa.heaps.top_k_frequent import top_k_frequent


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
        (([4, 4, 2, 2, 1], 2), [2, 4]),
        (([], 0), []),
        (([-1, -1, -2, -2], 2), [-2, -1]),
        (([1, 2], 0), []),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert top_k_frequent(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([1], 2), ([1], -1)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        top_k_frequent(*args)
