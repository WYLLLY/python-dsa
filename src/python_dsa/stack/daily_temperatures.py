"""Daily Temperatures. See problems/stack/daily_temperatures.md."""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return days until the next strictly warmer temperature."""
    result = [0] * len(temperatures)
    pending: list[int] = []
    for day, temperature in enumerate(temperatures):
        while pending and temperatures[pending[-1]] < temperature:
            previous = pending.pop()
            result[previous] = day - previous
        pending.append(day)
    return result
