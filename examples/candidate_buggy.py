def total_covered_length(intervals: list[tuple[int, int]]) -> int:
    # Intentionally flawed: assumes sorted input and mishandles nested overlaps.
    if not intervals:
        return 0
    total = 0
    left, right = intervals[0]
    for start, end in intervals[1:]:
        if start <= right:
            total += max(0, start - left)
            left, right = start, end
        else:
            total += right - left
            left, right = start, end
    return total + max(0, right - left)
