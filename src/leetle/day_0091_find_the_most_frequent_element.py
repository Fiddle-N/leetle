from collections import Counter


def solve(arr):
    if not arr:
        return None
    counter = Counter(arr)
    return counter.most_common()[0][0]
