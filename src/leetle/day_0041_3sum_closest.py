from itertools import combinations


def solve(nums, target):
    closest = None
    closest_sum = None

    for combo in combinations(nums, 3):
        diff = abs(sum(combo) - target)
        if closest is None or diff < closest:
            closest = diff
            closest_sum = sum(combo)
        if closest == 0:
            return closest_sum
    return closest_sum
