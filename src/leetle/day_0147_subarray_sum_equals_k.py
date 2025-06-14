import itertools


def solve(nums, k):
    # wrong way around
    nums, k = k, nums

    total = 0
    for start, end in itertools.combinations(range(len(nums) + 1), 2):
        seq = nums[start:end]
        if sum(seq) == k:
            total += 1
    return total
