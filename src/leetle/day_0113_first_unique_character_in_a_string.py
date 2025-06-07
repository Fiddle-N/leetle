from collections import Counter


def solve(s):
    count = Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1
