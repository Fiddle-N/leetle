from itertools import pairwise

def solve(intervals):
    sorted_intervals = sorted(
      intervals, 
      key=lambda interval: interval[0]
    )
    for (_, end_0), (start_1, _) in pairwise(sorted_intervals):
      if start_1 < end_0:
        return False
    return True
