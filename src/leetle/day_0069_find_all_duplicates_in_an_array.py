from collections import Counter


def solve(nums):
    counter = Counter(nums)
    dupes = []
    for num, count in counter.items():
        if count == 2:
            dupes.append(num)
    return sorted(dupes)
