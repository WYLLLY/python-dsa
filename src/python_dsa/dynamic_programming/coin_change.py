"""Coin Change. See problems/dynamic_programming/coin_change.md."""


def coin_change(coins: list[int], amount: int) -> int:
    """Return the fewest unlimited positive coins totaling amount, or -1."""
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be nonnegative and coins positive")
    unreachable = amount + 1
    best = [0] + [unreachable] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                best[total] = min(best[total], best[total - coin] + 1)
    return best[amount] if best[amount] != unreachable else -1
