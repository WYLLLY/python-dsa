"""Number of Islands. See problems/graphs/number_of_islands.md."""


def number_of_islands(grid: list[list[str]]) -> int:
    """Count four-neighbor components of '1' without modifying the grid."""
    columns = len(grid[0]) if grid else 0
    if any(len(row) != columns for row in grid):
        raise ValueError("grid must be rectangular")
    if any(cell not in {"0", "1"} for row in grid for cell in row):
        raise ValueError("cells must be '0' or '1'")
    seen: set[tuple[int, int]] = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(columns):
            if grid[row][col] != "1" or (row, col) in seen:
                continue
            islands += 1
            pending = [(row, col)]
            seen.add((row, col))
            while pending:
                r, c = pending.pop()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < columns
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        pending.append((nr, nc))
    return islands
