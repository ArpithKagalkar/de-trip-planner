from datetime import date


def trip_length_days(start: date, end: date) -> int:
    """Inclusive day count: 2025-01-01..2025-01-03 -> 3 days."""
    return (end - start).days + 1
