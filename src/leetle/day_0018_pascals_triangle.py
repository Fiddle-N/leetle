from itertools import pairwise


def solve(n):
    if n == 0:
        return []
    base = [[1]]
    for _ in range(1, n):
        last = base[-1]
        next_ = [1]
        for x in pairwise(last):
            next_.append(sum(x))
        next_.append(1)
        base.append(next_)
    return base
