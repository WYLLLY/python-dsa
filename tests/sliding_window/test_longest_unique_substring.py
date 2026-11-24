from copy import deepcopy

import pytest

from python_dsa.sliding_window.longest_unique_substring import longest_unique_substring


@pytest.mark.parametrize(
    "args, expected",
    [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("",), 0),
        (("abba",), 2),
        (("🙂é🙂a",), 3),
        (("pwwkew",), 3),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert longest_unique_substring(*args) == expected
    assert args == before
