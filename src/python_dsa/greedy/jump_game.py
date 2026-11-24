"""Jump Game. See problems/greedy/jump_game.md."""


def jump_game(jumps: list[int]) -> bool:
    """Return whether the last position is reachable from the first."""
    if any(jump < 0 for jump in jumps):
        raise ValueError("jumps must be nonnegative")
    if not jumps:
        return False
    farthest = 0
    for index, jump in enumerate(jumps):
        if index > farthest:
            return False
        farthest = max(farthest, index + jump)
        if farthest >= len(jumps) - 1:
            return True
    return False
