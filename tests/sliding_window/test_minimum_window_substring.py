from copy import deepcopy

import pytest

from python_dsa.sliding_window.minimum_window_substring import minimum_window_substring


@pytest.mark.parametrize(
    "args, expected",
    [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "aa"), ""),
        (("", "a"), ""),
        (("abc", ""), ""),
        (("aaab", "aab"), "aab"),
        (("abxba", "ab"), "ab"),
        (("é🙂é", "🙂é"), "é🙂"),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert minimum_window_substring(*args) == expected
    assert args == before


def test_matches_brute_force():
    from collections import Counter
    from itertools import product

    for size in range(6):
        for chars in product("ab", repeat=size):
            text = "".join(chars)
            for required in ("a", "b", "ab", "aa", "aab"):
                candidates = [
                    text[i:j]
                    for i in range(size)
                    for j in range(i + 1, size + 1)
                    if not Counter(required) - Counter(text[i:j])
                ]
                expected = min(candidates, key=len, default="")
                assert minimum_window_substring(text, required) == expected
