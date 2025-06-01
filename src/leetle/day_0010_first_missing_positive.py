from itertools import count


def solve(nums):
    num_set = set(nums)
    for num in count(start=1):
        if num not in num_set:
            return num
