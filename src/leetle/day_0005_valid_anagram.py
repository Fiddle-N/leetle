from collections import Counter


def solve(s1, s2):
    return Counter(s1) == Counter(s2)
