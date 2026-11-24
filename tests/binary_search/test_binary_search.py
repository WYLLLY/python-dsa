from copy import deepcopy

import pytest

from python_dsa.binary_search.binary_search import binary_search


@pytest.mark.parametrize(
    "args, expected",
    [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([1, 3], 2), -1),
        (([], 5), -1),
        (([4], 4), 0),
        (([1, 3, 5], 1), 0),
        (([1, 3, 5], 5), 2),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert binary_search(*args) == expected
    assert args == before
