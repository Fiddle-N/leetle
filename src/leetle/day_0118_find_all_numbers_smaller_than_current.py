def solve(nums):
    cum_counts = {}
    prev = 0
    prev_num = None
    for num in sorted(nums):
        if prev_num is None or num > prev_num:
            cum_counts[num] = prev
            prev_num = num
        prev += 1

    return [cum_counts[num] for num in nums]
