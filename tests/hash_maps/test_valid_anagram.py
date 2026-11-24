from copy import deepcopy

import pytest

from python_dsa.hash_maps.valid_anagram import valid_anagram


@pytest.mark.parametrize(
    "args, expected",
    [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("", ""), True),
        (("é🙂", "🙂é"), True),
        (("a", "aa"), False),
        (("A", "a"), False),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert valid_anagram(*args) == expected
    assert args == before
