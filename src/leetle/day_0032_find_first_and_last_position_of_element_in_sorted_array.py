import bisect


def solve(nums, target):
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    if left == right:
        # target not found:
        return [-1, -1]
    return [left, right - 1]
