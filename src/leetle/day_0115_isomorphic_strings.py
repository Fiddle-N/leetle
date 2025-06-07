from collections import Counter


def solve(s, t):
    # assume input is all lowercase ascii letters
    # also this solution broke ChatGPT
    return sorted(Counter(s).values()) == sorted(Counter(t).values())
