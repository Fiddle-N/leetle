from collections import Counter

def solve(jewels, stones):
    stone_count = Counter(stones)
    return sum([
        stone_count[jewel]
        for jewel in jewels
    ])
