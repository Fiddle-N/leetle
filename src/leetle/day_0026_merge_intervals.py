def solve(intervals):
    processed = intervals[:1]
    remaining = intervals[1:]
    while remaining:
        right = remaining.pop(0)
        for idx, left in enumerate(processed.copy()):
            if (left[0] <= right[1]) and (right[0] <= left[1]):
                # overlap
                merged_start = min(left[0], right[0])
                merged_end = max(left[1], right[1])
                merged = [merged_start, merged_end]
                processed[idx] = merged
                break
        else:
            processed.append(right)
    return processed
