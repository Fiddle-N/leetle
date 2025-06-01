import bisect


def solve(nums, target):
    if target not in nums:
        return -1
    return bisect.bisect_left(nums, target)
