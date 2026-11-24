from copy import deepcopy

import pytest

from python_dsa.dynamic_programming.coin_change import coin_change


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([], 0), 0),
        (([], 7), -1),
        (([2, 2, 3], 7), 3),
        (([1, 3, 4], 6), 2),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert coin_change(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([0], 0), ([-1, 2], 3), ([1], -1)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        coin_change(*args)


def test_matches_breadth_first_oracle():
    from collections import deque
    from itertools import combinations

    for size in range(4):
        for coins in combinations(range(1, 6), size):
            for amount in range(15):
                queue = deque([(0, 0)])
                seen = {0}
                expected = -1
                while queue:
                    total, steps = queue.popleft()
                    if total == amount:
                        expected = steps
                        break
                    for coin in coins:
                        nxt = total + coin
                        if nxt <= amount and nxt not in seen:
                            seen.add(nxt)
                            queue.append((nxt, steps + 1))
                assert coin_change(list(coins), amount) == expected
