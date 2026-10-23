def total_covered_length(intervals: list[tuple[int, int]]) -> int:
    valid = sorted((a, b) for a, b in intervals if a <= b)
    if not valid:
        return 0
    total = 0
    left, right = valid[0]
    for start, end in valid[1:]:
        if start == end:
            continue
        if start <= right:
            right = max(right, end)
        else:
            total += right - left
            left, right = start, end
    return total + right - left
