def total_covered_length(intervals: list[tuple[int, int]]) -> int:
    ranges = sorted((a, b) for a, b in intervals if a < b)
    if not ranges:
        return 0
    total = 0
    left, right = ranges[0]
    for start, end in ranges[1:]:
        if start <= right:
            right = max(right, end)
        else:
            total += right - left
            left, right = start, end
    return total + right - left
