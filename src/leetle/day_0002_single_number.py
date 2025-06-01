from collections import Counter

def solve(nums):
    return Counter(nums).most_common()[-1][0]
