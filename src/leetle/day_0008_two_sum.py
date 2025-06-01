from itertools import combinations


def solve(nums, target):
    for x, y in combinations(enumerate(nums), 2):
        if x[1] + y[1] == target:
            return sorted([x[0], y[0]])
    return []
