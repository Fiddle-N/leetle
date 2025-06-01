from itertools import pairwise


def solve(nums):
    if not nums:
        return 0

    sorted_nums = sorted(nums)
    curr = 1
    max_ = 1
    for x, y in pairwise(sorted_nums):
        curr = curr + 1 if y - x == 1 else curr if y - x == 0 else 1
        if curr > max_:
            max_ = curr
    return max_
