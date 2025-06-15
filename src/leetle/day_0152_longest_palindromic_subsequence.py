import itertools

def solve(s):
    if not s:
        return 0
    for n in range(len(s), 1, -1):
        for idxs in itertools.combinations(range(len(s)), n):
            subseq = [s[idx] for idx in idxs]
            if subseq == list(reversed(subseq)):
                return n
    return 1
 